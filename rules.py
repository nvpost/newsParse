def dateRules(name, date, title=False):
    if (name == "Atonics"):
        date = date.split(' ')[0]
    if name == "ООО «Стэнли» (Корунд)":
        date = date.split(' ')[0]
    if name == "Теплоприбор Челябинск":
        date = date.split(' ')[0]
    if name == 'Провенто':
        date = date + '.2022'
    if name == 'TDM ELECTRIC':
        date = date.replace('—', '2022')
    if (name == "Endress"):
        date = title.split(' ')[0]

    if (name == "Е_Е"):
        month_list = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November', 'December']
        for m in range(len(month_list)):
            old = month_list[m]
            date = date.replace(old, str(m + 1) + '.')

    return date
        
def imgRules(el, i, image_prefix):
    name = el['name']
    image_url=''
    try:
        if 'Phoenix contact' in name or 'APLISENS' in name or 'Теплоприбор Челябинск' in name or 'Schneider Electric' in name or 'Automate' in name or 'Werma' in name or 'teremonline.ru' in name:
            try:
                image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('style')).strip()
                image_url = image_url.replace(el['image_url']['replace_before'], '')
                image_url = image_url.replace(el['image_url']['replace_after'], '')
            except:
                pass
        elif 'Вектор ВС' in name:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data-bg-src'))
        elif 'Кип-сервис' in name or 'Werma' in name:
            image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data_1-src'))
        elif 'Полтраф СНГ' in name or 'Werma' in name or 'РИЗУР' in name or 'Aereco' in name:
            try:
                image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('data-src'))
            except:
                pass
        else:
            try:
                image_url = (i.select(el['image_url']['selector'])[el['image_url']['position']].get('src'))
            except:
                pass

        if image_url==None:
            image_url = el['default_image']
        else:
            image_url = image_prefix + image_url
    except:
        image_url = el['default_image']
    if image_url == '':
        image_url = el['default_image']
    return image_url