data = [
    {
        'category': 'Кип',
        'dop_cat': ['Кип', 'Датчики'],
        'place': 'ru',
        'id': 1,
        'name': 'Контравт',
        'url': "https://www.contravt.ru/news-KontrAvt",
        'url_prefix': 'https://www.contravt.ru',
        'root_': {
            'selector': "table.cell_standart_icon",
            'position': 0
        },
        'items_': {
            'selector': "td.cell_standart_icon_text",
            'position': 0
        },
        'date_': {
            'selector': "span.date_standart.date",
            'position': 0
        },
        'title_': {
            'selector': "a.menuchilds",
            'position': 1
        },
        'link_': {
            'selector': "a.short.detail",
            'position': 0
        }
    },
    {
        'category': 'Кип',
        'place': 'ru',
        'id': 2,
        'name': 'Atonics',
        'url': "https://www.autonics.com/company/ntt/news/list",
        'url_prefix': 'https://www.autonics.com/company/ntt/news/view/',
        'date_format': '%Y.%m.%d',
        'root_': {
            'selector': "ul.list-wrap",
            'position': 0
        },
        'items_': {
            'selector': "div.list-cont",
            'position': 0
        },
        'date_': {
            'selector': "span.tooltip-con",
            'position': 0
        },
        'title_': {
            'selector': "a.fc0",
            'position': 0
        },
        'link_': {
            'selector': "a.fc0",
            'position': 0
        },
        'options': {
            'link_type': 'javascript:view',
            'news_url': 'https://www.autonics.com/company/ntt/news/view/'
        }
    },

    {
        'category': 'Кип',
        'dop_cat': ['Кип', 'ОП', 'СПУ', 'ПЧВ'],
        'place': 'ru',
        'id': 3,
        'name': 'Deltronics',
        'url': "https://deltronics.ru/news/",
        'url_prefix': "https://deltronics.ru/",
        'root_': {
            'selector': "div.row.row-30",
            'position': 0
        },
        'items_': {
            'selector': "article.post-classic",
            'position': 0
        },
        'date_': {
            'selector': "div.unit-body",
            'position': 0
        },
        'title_': {
            'selector': "h5.post-classic-title",
            'position': 0
        },
        'link_': {
            'selector': "a.post-classic-figure",
            'position': 0
        }
    },
    {
        'category': 'Кип',
        'place': 'ru',
        'name': 'MZTA',
        'id': 4,
        'url': "https://www.mzta.ru/o-kompanii/novosti",
        'url_prefix': 'https://www.mzta.ru',
        'root_': {
            'selector': "ul.blog",
            'position': 0
        },
        'items_': {
            'selector': ".uk-grid",
            'position': 0
        },
        'date_': {
            'selector': "div.uk-width-1-4\@m",
            'position': 0
        },
        'title_': {
            'selector': "strong",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'Кип',
        'place': 'ru',
        'name': 'Трид',
        'id': 5,
        'url': "https://tridpm.ru/news",

        'root_': {
            'selector': "div.news-posts-wrapper",
            'position': 0
        },
        'items_': {
            'selector': "div.news-item",
            'position': 0
        },
        'date_': {
            'selector': "span.news-unit__date",
            'position': 0
        },
        'title_': {
            'selector': "h3.news-unit__title",
            'position': 0
        },
        'link_': False
    },
    {
        'category': 'Кип',
        'place': 'ru',
        'name': 'Autonics',
        'id': 6,
        'url': "https://www.ascontecnologic.com/блог/?lang=ru",

        'root_': {
            'selector': "div.slide-entry-wrap",
            'position': 0
        },
        'items_': {
            'selector': "article",
            'position': 0
        },
        'date_': {
            'selector': "time",
            'position': 0
        },
        'title_': {
            'selector': "h3.slide-entry-title",
            'position': 0
        },
        'link_': {
            'selector': "h3.slide-entry-title a",
            'position': 0
        }
    },
    {
        'category': 'Кип',
        'place': 'ru',
        'name': 'elemer',
        'id': 7,
        'url': "https://www.elemer.ru/news/",
        'url_prefix': 'https://www.elemer.ru/',
        'root_': {
            'selector': "div.news-list",
            'position': 0
        },
        'items_': {
            'selector': "div.news-item",
            'position': 0
        },
        'date_': {
            'selector': "span.news-date-time",
            'position': 0
        },
        'title_': {
            'selector': "a",
            'position': 1
        },
        'link_': {
            'selector': "a",
            'position': 1
        }
    },

    {
        'category': 'Кип',
        'place': 'ru',
        'name': 'Термодат',
        'id': 8,
        'url': "https://termodat.ru/information/news/",
        'url_prefix': 'https://termodat.ru/',
        'root_': {
            'selector': ".bx_news",
            'position': 0
        },
        'items_': {
            'selector': ".bx_news li",
            'position': 0
        },
        'date_': {
            'selector': ".date",
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

    # else
    {
        'category': 'Кип',
        'dop_cat': ['Кип'],
        'place': 'else',
        'id': '1',
        'name': 'Merret',
        'url': "https://www.merret.cz/en/news",
        'url_prefix': 'https://www.merret.cz',
        'date_format': '%d.%m.%Y',
        'root_': {
            'selector': "div.view-content div",
            'position': 0
        },
        'items_': {
            'selector': "div.news-inner-wrapper",
            'position': 0
        },
        'date_': {
            'selector': "div.views-field-field-news-date",
            'position': 0
        },
        'title_': {
            'selector': "div.views-field-title",
            'position': 0
        },
        'link_': {
            'selector': "span.field-content a",
            'position': 0
        }
    }
]



