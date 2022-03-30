data = [
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'EFK',
        'url': "https://ekfgroup.com/about/news",
        'url_prefix': 'https://ekfgroup.com',
        'root_': {
            'selector': "section.section-news",
            'position': 0
        },
        'items_': {
            'selector': "div.mb-sm-n16",
            'position': 0
        },
        'date_': {
            'selector': "span.published-at",
            'position': 0
        },
        'title_': {
            'selector': "div.card-news-item",
            'position': 0
        },
        'link_': {
            'selector': "a.card-body",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'Oni',
        'url': "https://oni-system.com/press-centr/",
        'url_prefix': 'https://oni-system.com',
        'root_': {
            'selector': "div.main_content",
            'position': 0
        },
        'items_': {
            'selector': "div.news",
            'position': 0
        },
        'date_': {
            'selector': "p.date",
            'position': 0
        },
        'title_': {
            'selector': "p.title",
            'position': 0
        },
        'link_': {
            'selector': "p.title a",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'Oni_IEK',
        'url': "https://oni-system.com/press-centr/novosti-IEK-GROUP.php",
        'url_prefix': 'https://oni-system.com',
        'root_': {
            'selector': "div.main_content",
            'position': 0
        },
        'items_': {
            'selector': "div.news",
            'position': 0
        },
        'date_': {
            'selector': "p.date",
            'position': 0
        },
        'title_': {
            'selector': "p.title",
            'position': 0
        },
        'link_': {
            'selector': "p.title a",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'Segnetics',
        'url': "https://segnetics.com/ru/news",
        'root_': {
            'selector': "table.main_table table",
            'position': 1
        },
        'items_': {
            'selector': "td",
            'position': 0
        },
        'date_': {
            'selector': ".news_item_date",
            'position': 0
        },
        'title_': {
            'selector': ".news_item_header",
            'position': 0
        },
        'link_': False
    },
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'Siemens',
        'url': "https://ru-siemens.com/news/",
        'root_': {
             'selector': "div.news__grid",
             'position': 0
        },
        'items_': {
             'selector': "div.col-md-6",
             'position': 0
        },
        'date_': {
             'selector': "span.news__item-time",
             'position': 0
        },
        'title_': {
             'selector': "h2.news__item-title",
             'position': 0
        },
        'link_': {
             'selector': "a.news__item",
             'position': 0
        }
    },
    # { //React
    #     'category': 'ПР',
    #     'place': 'com',
    #     'name': 'Danfoss',
    #     'url': "https://www.danfoss.com/ru-ru/about-danfoss/news/?sort=startDate_desc",
    #     'root_': {
    #         'selector': "div.list__wrapper",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "ul.news-list-items",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "div.tile__text-details",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "div.tile__text-title",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a.tile__image-link",
    #         'position': 0
    #     }
    # },
    {
        'category': 'ПР',
        'place': 'ru',
        'name': 'Eaton',
        'url': "http://www.eaton.ru/ru/ru-ru/company/news-insights/news-releases.html",
        'root_': {
            'selector': "div.results-list__content",
            'position': 0
        },
        'items_': {
            'selector': "div.results-list-submodule",
            'position': 0
        },
        'date_': {
            'selector': "div.results-list-submodule__date",
            'position': 0
        },
        'title_': {
            'selector': "h4.results-list-submodule__name",
            'position': 0
        },
        'link_': {
            'selector': "a.results-list-submodule__name-link",
            'position': 0
        }
    },

    {
        'category': 'ПР',
        'place': 'ru',
        'name': 'Omron',
        'url': "https://industrial.omron.ru/ru/news-events/news",
        'root_': {
            'selector': "section.magic-card",
            'position': 0
        },
        'items_': {
            'selector': "article.card",
            'position': 0
        },
        'date_': {
            'selector': "div.description strong",
            'position': 0
        },
        'title_': {
            'selector': "div.description",
            'position': 0
        },
        'link_': {
            'selector': "a.readmore",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'ru',
        'name': 'Carel',
        'url': "https://ru-carel.com/shopnews/",
        'url_prefix': '',
        'root_': {
            'selector': "ul.news__list",
            'position': 0
        },
        'items_': {
            'selector': "li.news__list-item",
            'position': 0
        },
        'date_': {
            'selector': "span.news__date",
            'position': 0
        },
        'title_': {
            'selector': "span.news__title",
            'position': 0
        },
        'link_': {
            'selector': "a.news__link",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'ru',
        'name': 'Агава',
        'url': "https://www.kb-agava.ru/index.php?route=information/news",
        'url_prefix': '',
        'root_': {
            'selector': "div#content",
            'position': 0
        },
        'items_': {
            'selector': "div.news_list_wrap",
            'position': 0
        },
        'date_': {
            'selector': "div.news_date",
            'position': 0
        },
        'title_': {
            'selector': "div.news_title",
            'position': 0
        },
        'link_': {
            'selector': "div.news_title a",
            'position': 0
        }
    },
    {
        'category': 'ПР',
        'place': 'com',
        'name': 'Danfoss',
        'url': "https://www.danfoss.com/uk-ua/about-danfoss/news/",
        'root_': {
            'selector': "body",
            'position': 0
        },
        'items_': {
            'selector': "li.tile",
            'position': 0
        },
        'date_': {
            'selector': "div.tile__text-details",
            'position': 0
        },
        'title_': {
            'selector': "div.tile__text-title",
            'position': 0
        },
        'link_': {
            'selector': "a.tile__image-link",
            'position': 0
        }
    },
]