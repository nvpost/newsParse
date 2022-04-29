from bs4 import BeautifulSoup
import requests
import datetime
import func
import parse_logic
from sql import send_data_sql



from data import sp_ru
from data import mt
from data import sensors
from data import op_ru
from data import kip
from data import p4v_ru
from data import pr
from data import agregator

from data_imgs import sp_ru
from data_imgs import mt
from data_imgs import sensors
from data_imgs import op_ru
from data_imgs import kip
from data_imgs import p4v_ru
from data_imgs import pr
from data_imgs import agregator


userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.769 Yowser/2.5 Safari/537.36"
addCounter = 0

an_chunks = [
    agregator.data,
    op_ru.data,
    pr.data,
    kip.data,
    sp_ru.data,
    p4v_ru.data,
    sensors.data,
    mt.data,

]


common_dateFormat = '%d.%m.%Y'


def doParse(cat):
    for el in cat:
        # if el['name']=='ASUTP':
        parse_logic.main_logic(el)




for cat in an_chunks:
    doParse(cat)










