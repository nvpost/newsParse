import datetime

def changeSymbol(s):
    s = s.replace('\xa0', ' ')
    return (s)


def df(date_str, format):
    return datetime.datetime.strptime(date_str, format)
