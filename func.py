import datetime

def changeSymbol(s):
    s = s.replace('\xa0', ' ')
    s = " ".join(s.split())

    return (s)


def df(date_str, format):
    date_str = date_str.replace(' г.', '')

    if date_str.find(" ")>0:

        month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']



        for m in range(len(month_list)):
            date_str = date_str.replace(',', '')
            date_str = date_str.lower()

            old = " "+month_list[m]+" "
            date_str = date_str.replace(old, '.'+str(m + 1)+'.')

    try:
        nd = datetime.datetime.strptime(date_str, format)[0:3]
    except:
        nd = date_str
    return nd
