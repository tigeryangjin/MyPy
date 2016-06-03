from datetime import datetime


def yang(date):
    print(type(date))
    b = datetime.strptime(date, '%Y-%m-%d')
    a = datetime(2016, 3, 12)
    print(a, b, a - b)


yang('2016-05-31')
