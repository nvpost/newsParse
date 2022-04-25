import datetime

def changeSymbol(s):
    s = s.replace('\xa0', ' ')
    s = " ".join(s.split())

    return (s)

def cleanDate(s):
    s = s.replace('\xa0', '')
    s = s.replace('\n', '')
    s = s.replace('\t', '')
    s = s.replace('|', '')
    s = s.replace('—', '2022')


    # Ломает дату
    s = s.replace(',', '')
    s = " ".join(s.split())
    s = s.replace(' ', '')
    return s


def date_exceptions(field, date):
    if (field == "Atonics"):
        date = date.split(' ')[0]
    if field == "ООО «Стэнли» (Корунд)":
        date = date.split(' ')[0]
    if field == "Теплоприбор Челябинск":
        date = date.split(' ')[0]
    if field == 'Провенто':
        date = date + '.2022'
    if field == 'TDM ELECTRIC':
        date = date.replace('—', '2022')

    if (field == "Е_Е"):
        month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        for m in range(len(month_list)):
            old = month_list[m]
            date = date.replace(old, str(m + 1) + '.')

    return date




def df(date_str, format):




    date_str = date_str.replace('/', '.')
    date_str = date_str.lower()

# есть даты в формате 24февраля2022

    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

    short_month_list = ['янв', 'февр', 'мар', 'апр', 'мая', 'июн',
                        'июл', 'авг', 'сент', 'окт', 'нояб', 'дек']

    month_list2 = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
                   'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    month_list_en = ['january', 'february', 'march', 'april', 'may', 'june',
                     'july', 'august', 'september', 'october', 'november', 'december']




    for m in range(len(month_list)):
        date_str = date_str.replace(', ', '')
        date_str = date_str.lower()

        old = month_list[m]
        date_str = date_str.replace(old, '.'+str(m + 1)+'.')

        # if date_str.find(" ") > 0:
    for m in range(len(month_list2)):
        old = month_list2[m]
        date_str = date_str.replace(old, '.' + str(m + 1) + '.')

    for m in range(len(short_month_list)):
        old = short_month_list[m]
        date_str = date_str.replace(old, '.' + str(m + 1) + '.')

    for m in range(len(month_list_en)):
        # print(m)
        date_str = date_str.replace(', ', '')
        date_str = date_str.lower()

        old = month_list_en[m]
        date_str = date_str.replace(old, '.' + str(m + 1) + '.')


    date_str = date_str.replace('г.', '')
    date_str = date_str.replace('..', '.')

    # print('---')
    # print('date_str',repr(date_str))
    # print('format', format)
    # print('---')

    # nd = datetime.datetime.strptime(date_str, format)
    try:
        nd = datetime.datetime.strptime(date_str, format)
    except:
        nd = date_str
    return nd
