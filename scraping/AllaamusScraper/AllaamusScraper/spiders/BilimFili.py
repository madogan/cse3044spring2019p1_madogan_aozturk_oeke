# -*- coding: utf-8 -*-

import scrapy
import requests

from bs4 import BeautifulSoup as bs


class BilimfiliSpider(scrapy.Spider):
    name = 'Bilimfili'
    allowed_domains = ['bilimfili.com']
    base_url = 'https://bilimfili.com'
    last_page_nums = dict()
    category_end_points = [
        # '/kategori/diger-bilimler/sinirbilim/',
        '/kategori/diger-bilimler/teknoloji/',
        '/kategori/diger-bilimler/psikoloji/',
        '/kategori/diger-bilimler/egitim/'
    ]

    def start_requests(self):
        for category_end_point in self.category_end_points:
            url = self.base_url + category_end_point
            last_page_num = BilimfiliSpider.get_last_page_num(url, category_end_point)
            for i in range(1, last_page_num + 1):
                url = self.base_url + category_end_point + f"page/{i}/"
                yield scrapy.Request(url=url, callback=self.parse, meta={"category_end_point": category_end_point})

    def parse(self, response):
        posts = response.css(".categoryPostListTab")
        for post in posts:
            post_url = post.css(".simpleLink")[0].attrib["href"]
            yield scrapy.Request(url=post_url,
                                 callback=self.parse_content,
                                 meta={"category_end_point": response.meta["category_end_point"]})

    def parse_content(self, response):
        yield {
            "source": "bilimfili.com",
            "url": response.url,
            "category": response.meta["category_end_point"].split("/")[-2],
            "date": response.css(".singlePostTabLeftTop .simpleDate::text")[0].get(),
            "title": response.css("h1.title::text").get(),
            "content": " ".join([bs(p.get(), "lxml").get_text() for p in response.css(".pageDetailContent p")]).strip(),
            "tags": [t.css("a::text").get() for t in response.css(".listTags ul li")]   
        }

    @staticmethod
    def get_last_page_num(_url, _category_end_point):
        print(_url)
        resp = requests.get(_url)
        tree = bs(resp.content, "lxml")
        return int(tree.select(".newPagination li")[-2].select("a")[0].get_text())
