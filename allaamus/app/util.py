import datetime


def date_str_to_datetime_for_bilimfili(ds):
    MONTHS = {
        "ocak": 1,
        "şubat": 2,
        "mart": 3,
        "nisan": 4,
        "mayıs": 5,
        "haziran": 6,
        "temmuz": 7,
        "ağustos": 8,
        "eylül": 9,
        "ekim": 10,
        "kasım": 11,
        "aralık": 12
    }
    splitted =  ds.split()  # "18 Aralık 2018" --> ["18", "Aralık", "2018"]
    
    day = int(splitted[0].strip())
    month = MONTHS[splitted[1].strip().lower()]
    year = int(splitted[2].strip())

    return datetime.datetime(year, month, day)
