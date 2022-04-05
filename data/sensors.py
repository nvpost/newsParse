data = [
    {
        # Ставим дату как есть
        'category': 'Датчики',
        'place': 'ru',
        'id': '0',
        'name': 'ТЕККНОУ',
        'url': "https://www.tek-know.ru/news/",
        'url_prefix': 'https://www.tek-know.ru',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "div.item",
            'position': 0
        },
        'date_': False,
        # 'date_': {
        #     'selector': "span.date",
        #     'position': 0
        # },
        'title_': {
            'selector': "h3",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        # Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '1',
        'name': 'Seitron',
        'url': "https://www.seitron.ru/novosti.html",
        'url_prefix': 'https://www.seitron.ru/',
        'root_': {
            'selector': "div.blog-content",
            'position': 0
        },
        'items_': {
            'selector': "div.items-row",
            'position': 0
        },
        # 'date_': {
        #     'selector': "",
        #     'position': 0
        # },
        'date_': False,
        'title_': {
            'selector': "h2",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        # Без даты, дата в заголовках
        'category': 'Датчики',
        'place': 'com',
        'id': '2',
        'name': 'Endress',
        'url': "https://www.ru.endress.com/ru/media-center/newsroom",
        'url_prefix': 'https://www.ru.endress.com',
        'root_': {
            'selector': "ul.eh-search-result--results-items",
            'position': 0
        },
        'items_': {
            'selector': "li.eh-search-result--results-item--02",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "p",
            'position': 0
        },
        'link_': {
            'selector': "a.eh-link--03",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '3',
        'name': 'Phoenix contact',
        'url': "https://www.phoenixcontactpro.ru/about/news/",
        'url_prefix': 'https://www.phoenixcontactpro.ru',
        'root_': {
            'selector': "div.content-block",
            'position': 0
        },
        'items_': {
            'selector': "div.news-item",
            'position': 0
        },
        'date_': {
            'selector': "div.date span",
            'position': 0
        },
        'title_': {
            'selector': "a.name",
            'position': 0
        },
        'link_': {
            'selector': "a.image",
            'position': 0
        }
    },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'com',
        'id': '4',
        'name': 'PEPPERL_FUCHS',
        'url': "https://www.pepperl-fuchs.com/russia/ru/22690.htm",
        'url_prefix': 'https://www.pepperl-fuchs.com',
        'root_': {
            'selector': "div.container_news_box",
            'position': 0
        },
        'items_': {
            'selector': "div.link-text-img",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "div.title",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    #     {
    #     'category': 'Датчики',
    #     'place': 'com',
    #     'id': '5',
    #     'name': 'LEFOO',
    #     'url': "https://www.lefoo.com/news",
    #     'url_prefix': '',
    #     'root_': {
    #         'selector': "ul.industify_fn_postlist",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "div.content_holder",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "p.t_header",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "h3",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # },
    {
        'category': 'Датчики',
        'place': 'com',
        'id': '6',
        'name': 'Huba Control',
        'url': "https://www.hubacontrol.com/ru/biznes/novosti",
        'url_prefix': 'https://www.hubacontrol.com',
        'root_': {
            'selector': "div.news-list-wrapper",
            'position': 0
        },
        'items_': {
            'selector': "div.description",
            'position': 0
        },
        'date_': {
            'selector': "p",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'com',
        'id': '7',
        'name': 'Е_Е',
        'url': "https://www.epluse.com/press/press-releases/",
        'url_prefix': 'https://www.epluse.com',
        # 'root_': {
        #     'selector': "ul.news-list-container",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': "li.news-list-item",
            'position': 0
        },
        'date_': {
            'selector': "h3",
            'position': 0
        },
        'title_': {
            'selector': "h2",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    #     {
    #     #     JS
    #     'category': 'Датчики',
    #     'place': 'ru',
    #     'id': '8',
    #     'name': 'Элемер',
    #     'url': "https://www.elemer.ru/news/",
    #     'url_prefix': 'https://www.elemer.ru',
    #     # 'root_': {
    #     #     'selector': "div.news-list",
    #     #     'position': 0
    #     # },
    #     'root_':False,
    #     'items_': {
    #         'selector': "div.news-item",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "span",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "a",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '9',
        'name': 'Эксис',
        'url': "https://www.eksis.ru/news/company/",
        'url_prefix': 'https://www.eksis.ru',
        'root_': {
            'selector': "div.centcol ",
            'position': 0
        },
        'items_': {
            'selector': "div.t_date",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        #     Ограниченое количество новостей
        'category': 'Датчики',
        'place': 'ru',
        'id': '10',
        'name': 'BD Sensors',
        'url': "https://www.bdsensors.ru/ru/kompaniya/novosti-kompanii/",
        'url_prefix': 'https://www.bdsensors.ru/',
        # 'root_': {
        #     'selector': "div.news",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': ".article",
            'position': 0
        },
        'date_': {
            'selector': ".news-list-date",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '11',
        'name': 'APLISENS',
        'url': "https://www.aplisens.ru/news/",
        'url_prefix': 'https://www.aplisens.ru',
        'root_': {
            'selector': "div.row",
            'position': 0
        },
        'items_': {
            'selector': "div.news-item",
            'position': 0
        },
        'date_': {
            'selector': "span.date",
            'position': 0
        },
        'title_': {
            'selector': "p.news-title",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '12',
        'name': 'Аналитприбор',
        'url': "https://www.analitpribor-smolensk.ru/company/novosti/",
        'url_prefix': 'https://www.analitpribor-smolensk.ru',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "div.news-list__item",
            'position': 0
        },
        'date_': {
            'selector': "div.news-list__date",
            'position': 0
        },
        'title_': {
            'selector': "div.news-list__title",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '13',
        'name': 'Aereco',
        'url': "https://www.aereco.ru/aereco/novosti/",
        'url-prefix': '',
        'root_': {
            'selector': "div.items-specify-mobile",
            'position': 0
        },
        'items_': {
            'selector': "article",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "h2",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '14',
        'name': 'Vega',
        'url': "https://vega-rus.ru/news/",
        'url_prefix': 'https://vega-rus.ru',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "p.news-item",
            'position': 0
        },
        'date_': {
            'selector': "span",
            'position': 0
        },
        'title_': {
            'selector': "b",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '15',
        'name': 'Вакууммаш',
        'url': "https://vakuummash.ru/category/press-center/",
        'url-prefix': '',
        # 'root_': {
        #     'selector': "div.news-block",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': "div.item",
            'position': 0
        },
        'date_': {
            'selector': "span.color-5",
            'position': 0
        },
        'title_': {
            'selector': "a.d-block",
            'position': 0
        },
        'link_': {
            'selector': "a.d-block",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '16',
        'name': 'Теко',
        'url': "https://teko-com.ru/news/",
        'url-prefix': '',
        'root_': {
            'selector': "div.oformleniecont",
            'position': 0
        },
        'items_': {
            'selector': "div.caption",
            'position': 0
        },
        'date_': {
            'selector': "div",
            'position': 0
        },
        'title_': {
            'selector': "h4",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '17',
        'name': 'Русавтоматизация',
        'url': "https://rusautomation.ru/company/news/",
        'url_prefix': 'https://rusautomation.ru',
        'root_': {
            'selector': "div.news-blog-custom",
            'position': 0
        },
        'items_': {
            'selector': "div.body-info",
            'position': 0
        },
        'date_': {
            'selector': "span",
            'position': 0
        },
        'title_': {
            'selector': "a.dark-color",
            'position': 0
        },
        'link_': {
            'selector': "a.dark-color",
            'position': 0
        }
    },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '18',
        'name': 'Росма',
        'url': "https://rosma.spb.ru/news/",
        'url_prefix': 'https://rosma.spb.ru/',
        'root_': {
            'selector': "div.news",
            'position': 0
        },
        'items_': {
            'selector': "li.news__item",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '19',
        'name': 'РИЗУР',
        'url': "https://rizur.ru/company/news/",
        'url_prefix': 'https://rizur.ru',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "div.item-content",
            'position': 0
        },
        'date_': {
            'selector': "div.item-date",
            'position': 0
        },
        'title_': {
            'selector': "div.item-title",
            'position': 0
        },
        'link_': {
            'selector': 'a[href^="/company/"]',
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'com',
        'id': '20',
        'name': 'Рэлсиб',
        'url': "https://relsib.com/news",
        'url-prefix': '',
        # 'root_': {
        #     'selector': "div.col-md-12",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': "div.news",
            'position': 0
        },
        'date_': {
            'selector': "div.news-date",
            'position': 0
        },
        'title_': {
            'selector': "div.news-title",
            'position': 0
        },
        'link_': {
            'selector': "a.more",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '21',
        'name': 'Raimet',
        'url': "https://raimet.ru/information/news",
        'url_prefix': 'https://raimet.ru',
        'root_': {
            'selector': "div.swiper-wrapper",
            'position': 0
        },
        'items_': {
            'selector': "div.swiper-slide",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "div.description",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '22',
        'name': 'Pribor-r',
        'url': "https://pribor-r.ru/news/",
        'url_prefix': 'https://pribor-r.ru',
        'root_': {
            'selector': "ul.news-list",
            'position': 0
        },
        'items_': {
            'selector': "div.c",
            'position': 0
        },
        'date_': {
            'selector': "div.d",
            'position': 0
        },
        'title_': {
            'selector': "a.n",
            'position': 0
        },
        'link_': {
            'selector': "a.n",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '23',
        'name': 'Pulsar',
        'url': "https://pulsarm.ru/o-kompanii/novosti/",
        'url_prefix': 'https://pulsarm.ru',
        'root_': {
            'selector': "div.section-news",
            'position': 0
        },
        'items_': {
            'selector': "div.news",
            'position': 0
        },
        # 'date_': False,
        'date_': {
            'selector': "div.date false",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '24',
        'name': 'Полтраф СНГ',
        'url': "https://poltraf.ru/about/news/",
        'url_prefix': 'https://poltraf.ru',
        'root_': {
            'selector': "div.s_4",
            'position': 0
        },
        'items_': {
            'selector': "div.inner-text",
            'position': 0
        },
        'date_': {
            'selector': "span",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    #     {
    #     'category': 'Датчики',
    #     'place': 'ru',
    #     'id': '25',
    #     'name': 'Packo',
    #     'url': "https://packo.ru/novosti",
    #     'url-prefix': '',
    #     'root_': {
    #         'selector': "div.news_block_cont",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "a.news_block2",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "span.news_date",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "span.news_block_title_i",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a.news_block2",
    #         'position': 0
    #     }
    # },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '25',
        'name': 'Мераприбор',
        'url': "https://merapribor.ru/info/news/",
        'url_prefix': 'https://merapribor.ru',
        'root_': {
            'selector': "div.items",
            'position': 0
        },
        'items_': {
            'selector': "div.col-md-8",
            'position': 0
        },
        'date_': {
            'selector': "span.label",
            'position': 0
        },
        'title_': {
            'selector': "div.title",
            'position': 0
        },
        'link_': {
            'selector': "a.btn-default",
            'position': 0
        }
    },

    #     {
    #     #     Страница недоступна
    #     'category': 'Датчики',
    #     'place': 'ru',
    #     'id': '26',
    #     'name': 'Кип-сервис',
    #     'url': "https://kipservis.ru/news",
    #     'url_prefix': 'https://kipservis.ru',
    #     'root_': {
    #         'selector': "div.cards",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "li.card",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "small",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "a",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '27',
        'name': 'КЕАЗ',
        'url': "https://keaz.ru/company/press-center/news",
        'url-prefix': '',
        'root_': {
            'selector': "div.content",
            'position': 0
        },
        'items_': {
            'selector': "div.info-content__description",
            'position': 0
        },
        'date_': {
            'selector': "div.info-content__text_bold false",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '28',
        'name': 'ИЗМЕРКОН («Измерение и Контроль») KELLER',
        'url': "https://izmerkon.ru/about/news/",
        'url_prefix': 'https://izmerkon.ru',
        'root_': {
            'selector': "div.rows",
            'position': 0
        },
        'items_': {
            'selector': "div.article_news",
            'position': 0
        },
        'date_': {
            'selector': "p",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '29',
        'name': 'E_E su',
        'url': "https://epluse.su/news/news.htm",
        'url_prefix': 'https://epluse.su',
        'root_': {
            'selector': "div.akc",
            'position': 0
        },
        'items_': {
            'selector': "div.novost",
            'position': 0
        },
        'date_': {
            'selector': "div.textdate",
            'position': 0
        },
        'title_': {
            'selector': "div.text",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '30',
        'name': 'Dwyer',
        'url': "https://dwyer.ru/nashi-novosti",
        'url_prefix': 'https://dwyer.ru',
        'root_': {
            'selector': "div.blog",
            'position': 0
        },
        'items_': {
            'selector': "div.page-header",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "h2",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '31',
        'name': 'Цит плюс',
        'url': "https://cit-plus.ru/o-kompanii/press-czentr/novosti/",
        'url-prefix': '',
        'root_': {
            'selector': "div.company--width",
            'position': 0
        },
        'items_': {
            'selector': "div.company__item",
            'position': 0
        },
        'date_': {
            'selector': "div.company__item-date",
            'position': 0
        },
        'title_': {
            'selector': "div.title",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '32',
        'name': 'Компания «БД»',
        'url': "https://bdrosma.ru/news/",
        'url_prefix': 'https://bdrosma.ru/',
        'root_': {
            'selector': "main.news_list",
            'position': 0
        },
        'items_': {
            'selector': "div.news_page_item",
            'position': 0
        },
        'date_': {
            'selector': "span.date",
            'position': 0
        },
        'title_': {
            'selector': "span.descr",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '33',
        'name': 'Альбатрос',
        'url': "https://albatros.ru/news/archive/",
        'url_prefix': 'https://albatros.ru',
        'root_': {
            'selector': "div.front_news_list",
            'position': 0
        },
        'items_': {
            'selector': "div.front-news-body",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "div.news-title",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '34',
        'name': 'Yokogawa',
        'url': "http://www.yokogawa.ru/news/",
        'url_prefix': 'http://www.yokogawa.ru',
        # 'root_': {
        #     'selector': "div.news_list",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': "div.news_list > div.item",
            'position': 0
        },
        'date_': {

            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "div.anons > a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '35',
        'name': 'Термоконт',
        'url': "http://www.termiko.ru/news/",
        'url_prefix': 'http://www.termiko.ru',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "p.news-item",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "b",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '36',
        'name': 'Эталон Омск',
        'url': "http://www.omsketalon.ru/novosti",
        'url_prefix': 'http://www.omsketalon.ru',
        'date_format': '%d.%m.%y',
        # 'root_': {
        #     'selector': "div.col-md_news",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': ".block_news_fon",
            'position': 0
        },
        'date_': {
            'selector': "div.data_news",
            'position': 0
        },
        'title_': {
            'selector': "div.zag_news",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '37',
        'name': 'ООО «Стэнли» (Корунд)',
        'url': "https://stenli.ru/novosti",
        'url_prefix': 'https://stenli.ru/',
        'date_format': '%d.%m.%Y',
        'root_': {
            'selector': "div.g-article-list",
            'position': 0
        },
        'items_': {
            'selector': "article.g-article",
            'position': 0
        },
        'date_': {
            'selector': "time",
            'position': 0
        },
        'title_': {
            'selector': "a.g-article__name",
            'position': 0
        },
        'link_': {
            'selector': "a.g-article__name",
            'position': 0
        }
    },
    {
        'category': 'Датчики',
        'place': 'ru',
        'id': '38',
        'name': 'Теплоприбор Челябинск',
        'url': "http://tpchel.ru/articles/categories/1",
        'url-prefix': '',
        'root_': {
            'selector': "div.slim-articles-list",
            'position': 0
        },
        'items_': {
            'selector': "a.item",
            'position': 0
        },
        'date_': {
            'selector': "div.date",
            'position': 0
        },
        'title_': {
            'selector': "div.title",
            'position': 0
        },
        'link_': {
            'selector': "",
            'position': 0
        }
    },
    {
        #     без даты
        'category': 'Датчики',
        'place': 'com',
        'id': '39',
        'name': 'Мида',
        'url': "http://midaus.com/",
        'url_prefix': 'http://midaus.com',
        'root_': {
            'selector': "div.allnews",
            'position': 0
        },
        'items_': {
            'selector': "h4.newsflash-title",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        #     Без даты
        'category': 'Датчики',
        'place': 'ru',
        'id': '40',
        'name': 'Ленпромавтоматика',
        'url': "http://lpadevice.ru/new/",
        'url-prefix': '',
        'root_': {
            'selector': "table.newstable",
            'position': 0
        },
        'items_': {
            'selector': "tr.newstable",
            'position': 0
        },
        'date_': {
            'selector': "",
            'position': 0
        },
        'title_': {
            'selector': "a.title",
            'position': 0
        },
        'link_': {
            'selector': "a.title",
            'position': 0
        }
    },
    {
        # Таблицы
        'category': 'Датчики',
        'place': 'ru',
        'id': '',
        'name': 'Real Lab (РФ)11',
        'url': "https://www.reallab.ru/news/",
        'url_prefix': 'https://',
        # 'root_': {
        #     'selector': "div.naviText",
        #     'position': 0
        # },
        'root_': False,
        'items_': {
            'selector': "table",
            'position': 0
        },
        'date_': {
            'selector': "strong false",
            'position': 0
        },
        'title_': {
            'selector': "p",
            'position': 0
        },
        'link_': {
            'selector': "a.Header2Link",
            'position': 0
        }
    },
    # собирает js
    #     {
    #     'category': 'Датчики',
    #     'place': 'ru',
    #     'id': '',
    #     'name': 'Piezus',
    #     'url': "https://piezus.ru/blog/cat/news",
    #     'root_': {
    #         'selector': "div.col-main",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "div.row",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "span.d-date",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "p",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a.magentothem-blog-read-more",
    #         'position': 0
    #     }
    # },

    {
        'category': 'Датчики',
        'dop_cat': ['Датчики', 'ОП'],
        'place': 'ua',
        'id': '1',
        'name': 'CarelUA',
        'url': "https://www.carel.ua/news",
        'url_prefix': '',
        'date_format': '%d.%m.%Y',
        'root_': False,
        'items_': {
            'selector': "div.asset-news-content",
            'position': 0
        },
        'date_': {
            'selector': "div.news-date",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    }
]
