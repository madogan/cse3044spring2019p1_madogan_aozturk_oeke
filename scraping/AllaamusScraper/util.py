import datetime


def bilimfili_date_str_to_datetime(t):
    MONTHS = {
        "Ocak": 1,
        "Şubat": 2,
        "Mart": 3,
        "Nisan": 4,
        "Mayıs": 5,
        "Haziran": 6,
        "Temmuz": 7,
        "Ağustos": 8,
        "Eylül": 9,
        "Ekim": 10,
        "Kasım": 11,
        "Aralık": 12
    }

    day = int(t.split()[0].strip())
    month = int(MONTHS[t.split()[1].strip()])
    year = int(t.split()[2].strip())

    return datetime.datetime(year, month, day)
