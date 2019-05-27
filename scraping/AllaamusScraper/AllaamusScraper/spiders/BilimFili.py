# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup as bs


class BilimfiliSpider(scrapy.Spider):
    name = 'BilimFili'
    allowed_domains = ['bilimfili.com']
    base_url = 'https://bilimfili.com/kategori/diger-bilimler/'
    last_page_nums = dict()
    categories = [
        'teknoloji', 
        'psikoloji',
        'egitim'
    ]

    def start_requests(self):
        for category in self.categories:
            _url = self.base_url + category
            resp = requests.get(_url)
            tree = bs(resp.content, "lxml")
            self.last_page_nums[category] = int(tree.select(".newPagination li")[-2].select("a")[0].get_text())
            yield scrapy.Request(url=_url, callback=self.parse, meta={"category": category})

    def parse(self, response):
        print("deneme_", response.url)
        posts = response.css(".categoryPostListTab")
        
        for post in posts:
            post_url = post.css(".simpleLink")[0].attrib["href"]
            yield scrapy.Request(url=post_url, callback=self.parse_content, meta={"category": response.meta["category"]})


        if "/page/" in response.url:
            current_page_num = int(response.url.split("/")[-2])
        else:
            current_page_num = 2

        if current_page_num <= self.last_page_nums[response.meta["category"]]:
            next_page_url = self.base_url + response.meta["category"] + "/page/" + str(current_page_num)
            scrapy.Request(next_page_url, callback=self.parse, meta={"category": response.meta["category"]})

    def parse_content(self, response):
        yield {
            "source": "bilimfili.com",
            "url": response.url,
            "category": response.meta["category"],
            "date": response.css(".singlePostTabLeftTop .simpleDate::text")[0].get(),
            "title": response.css("h1.title::text").get(),
            "content": " ".join([bs(p.get(), "lxml").get_text() for p in response.css(".pageDetailContent p")]).strip(),
            "tags": [t.css("a::text").get() for t in response.css(".listTags ul li")]   
        }
