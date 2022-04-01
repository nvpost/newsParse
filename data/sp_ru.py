data = [
    # https://press.siemens.ru/search/?fl41942=55175
    {
        'category': 'СПУ',
        'dop_cat': ['СПУ', 'ПЧВ'],
        'place': 'ru',
        'id': '0',
        'name': 'Schneider Electric',
        'url': "https://www.se.com/ru/ru/about-us/newsroom/news/",
        'url_prefix': "https://www.se.com",
        'root_': {
            'selector': "section.sdl-wiztopic-press-releases",
            'position': 0
        },
        'items_': {
            'selector': "div.sdl-wiztopic-press-releases_wiztopic-card",
            'position': 0
        },
        'date_': {
            'selector': "div.date-published",
            'position': 0
        },
        'title_': {
            'selector': "p",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    # {
    #     # JS
    #     'category': 'СПУ',
    #     'place': 'ru',
    #     'id': '1',
    #     'name': 'Beckhoff',
    #     'url': "https://www.beckhoff.com/ru-ru/company/news/",
    #     'url_prefix': "https://www.beckhoff.com",
    #     'root_': {
    #         'selector': ".news.news--list",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': ".news__item-body",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "p.text-small",
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
        'category': 'СПУ',
        'place': 'ru',
        'id': '2',
        'name': 'ICP-DAS',
        'url': "https://icp-das.ru/blogs/news",
        'url_prefix': "https://icp-das.ru",
        'date_format': '.%m.%d%Y',
        'root_': {
            'selector': "ul.blog--inner",
            'position': 0
        },
        'items_': {
            'selector': "li.article--excerpt-wrapper  ",
            'position': 0
        },
        'date_': {
            'selector': "div.article--excerpt-meta",
            'position': 0
        },
        'title_': {
            'selector': "h2.article--excerpt-title",
            'position': 0
        },
        'link_': {
            'selector': "a.article--excerpt-image",
            'position': 0
        }
    },
    {
        'category': 'СПУ',
        'place': 'ru',
        'id': '3',
        'name': 'MOXA',
        'url': "https://moxa.ru/novosti/",
        'url_prefix': "https://moxa.ru",
        'root_': {
            'selector': "div.newpage",
            'position': 0
        },
        'items_': {
            'selector': "div.techbox",
            'position': 0
        },
        'date_': {
            'selector': "div.newsbox_date",
            'position': 0
        },
        'title_': {
            'selector': "div.usebox_name",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'СПУ',
        'place': 'ru',
        'id': '4',
        'name': 'Прософт-Системы',
        'url': "https://prosoftsystems.ru/news",
        'url_prefix': "https://prosoftsystems.ru",
        'root_': {
            'selector': "div.articles",
            'position': 0
        },
        'items_': {
            'selector': "div.articles-item-inner",
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
        'category': 'СПУ',
        'place': 'com',
        'id': '5',
        'name': 'Mitsubishi Electric',
        'url': "https://ru.mitsubishielectric.com/ru/news/index.html",
        'url_prefix': "https://ru.mitsubishielectric.com",
        'root_': {
            'selector': "ul.gs18-BorderedDateLinkList",
            'position': 0
        },
        'items_': {
            'selector': "li.gs18-BorderedDateLinkListItem",
            'position': 0
        },
        'date_': {
            'selector': "p.gs18-Date",
            'position': 0
        },
        'title_': {
            'selector': "p.gs18-Text",
            'position': 0
        },
        'link_': {
            'selector': "a.gs18-Link",
            'position': 0
        }
    },
    {
        'category': 'СПУ',
        'place': 'digital',
        'id': '6',
        'name': 'Tibbo Systems',
        'url': "https://blog.aggregate.digital/ru/category/company-news/",
        'date_format': '.%d.%m%Y',
        'root_': {
            'selector': "main.site-main",
            'position': 0
        },
        'items_': {
            'selector': "article",
            'position': 0
        },
        'date_': {
            'selector': "time.published",
            'position': 0
        },
        'title_': {
            'selector': "header",
            'position': 0
        },
        'link_': {
            'selector': "a.post-thumbnail",
            'position': 0
        }
    },
    # собирает js
    # {
    #     'category': 'СПУ',
    #     'place': 'ru',
    #     'id': '',
    #     'name': 'Weintek',
    #     'url': "https://weintek.ru/#rec301663737",
    #     'url-prefix': "",
    #     'root_': {
    #         'selector': "body",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "div.t-feed__col-grid__content",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "span.js-feed-post-date",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "div.js-feed-post-title",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a.js-feed-post-link",
    #         'position': 0
    #     }
    # },
    # собирает js
    # {
    #     'category': 'СПУ',
    #     'place': 'ru',
    #     'id': '',
    #     'name': 'Siemens',
    #     'url': "https://press.siemens.ru/search/?fl41942=55175",
    #     'url-prefix': "",
    #     'root_': {
    #         'selector': "div.contentNews-1",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': "div.press-search-results-view-row",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': "div.search-result-footer-event-meta",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': "div.views-field views-field-title",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # }
]
