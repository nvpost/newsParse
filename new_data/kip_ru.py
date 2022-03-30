base = [
    {
        'category': 'Кип',
        'place': 'ru',
        'id': '1',
        'name': 'Контравт',
        'url': "https://www.contravt.ru/news-KontrAvt",
        'url-prefix': 'https://www.contravt.ru/',
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
        'id': '2',
        'name': 'MZTA',
        'url': "https://www.mzta.ru/o-kompanii/novosti",
        'url-prefix': 'https://www.mzta.ru/',
        'root_': {
            'selector': "ul.blog",
            'position': 0
        },
        'items_': {
            'selector': "div.uk-grid",
            'position': 0
        },
        'date_': {
            'selector': "div",
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
        'id': '3',
        'name': 'Трид',
        'url': "https://tridpm.ru/news",
        'url-prefix': '',
        'root_': {
            'selector': "div.news-posts",
            'position': 0
        },
        'items_': {
            'selector': "div.news-unit__info",
            'position': 0
        },
        'date_': {
            'selector': "span.news-unit__date",
            'position': 0
        },
        'title_': {
            'selector': "h3.news-unit__title_big",
            'position': 0
        },
        'link_': {
            'selector': "",
            'position': 0
        }
    },
    #
    {
        'category': 'Кип',
        'place': 'ru',
        'id': '4',
        'name': 'Deltronics',
        'url': "https://deltronics.ru/news/",
        'url-prefix': 'https://deltronics.ru/',
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
    }
]
