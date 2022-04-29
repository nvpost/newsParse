data = [
    # 1
    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'cityron',
        'id': 1,
        'url': "https://cityron.ru/novosti",
        'default_image': "https://cityron.ru/assets/web/_cache/thumbs/assets/mgr/images/logo_270x48_623.png",
        "url_prefix": "https://cityron.ru/",
        'root_': {
            'selector': "#news",
            'position': 0
        },
        'items_': {
            'selector': ".news-panel",
            'position': 0
        },
        'date_': {
            'selector': ".info-date",
            'position': 0
        },
        'title_': {
            'selector': ".info-title",
            'position': 0
        },
        'link_': {
            'selector': "_self_item_",
            'position': 0
        },
        'image_url': {
            'selector': "img",
            'position': 0,
            'image_prefix': 'https://cityron.ru'
        }
    },
{
        'category': 'ОП',
        'place': 'ru',
        'name': 'electrotest',
        'id': 2,
        'url': "https://electrotest.ru/about/news/",
        'default_image': "https://electrotest.ru/assets/images/bl.svg",
        'url_prefix': 'https://electrotest.ru/',
        'root_': {
            'selector': ".tabs__content.active",
            'position': 0
        },
        'items_': {
            'selector': ".news_item",
            'position': 0
        },
        'date_': {
            'selector': ".news-d",
            'position': 0
        },
        'title_': {
            'selector': ".news-t",
            'position': 0
        },
        'link_': {
            'selector': ".news-t a",
            'position': 0
        },
        'image_url': {
            'selector': "img",
            'position': 0,
            'image_prefix': 'https://electrotest.ru/'
        }
    },
# {
#     В ПР
#         'category': 'ОП',
#         'place': 'ru',
#         'name': 'segnetics',
#         'id': 3,
#         'url': "https://segnetics.com/ru/news",
#         'date_format': '%d.%m.%y',
#         'root_': {
#             'selector': ".main_table table",
#             'position': 0
#         },
#         'items_': {
#             'selector': "tr",
#             'position': 0
#         },
#         'date_': {
#             'selector': ".news_item_date",
#             'position': 0
#         },
#         'title_': {
#             'selector': ".news_item_header",
#             'position': 0
#         },
#         'link_': False
#     },

    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'bolid',
        'id': 5,
        'url': "https://bolid.ru/about/news/",
        'default_image': "https://bolid.ru/bld/images/logo.png",
        'url_prefix': 'https://bolid.ru',
        'date_format': '%d.%m.%Y',
        'root_': {
            'selector': ".cont_inner_right",
            'position': 0
        },
        'items_': {
            'selector': ".news_page",
            'position': 0
        },
        'date_': {
            'selector': ".news_date",
            'position': 0
        },
        'title_': {
            'selector': ".news_text",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        }
    },
    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'moemgorod.com',
        'id': 7,
        'url': "https://moemgorod.com/blog/",
        'default_image': "https://moemgorod.com/wa-data/public/site/themes/supreme/img/logo.png",
        'root_': {
            'selector': "#post-stream",
            'position': 0
        },
        'items_': {
            'selector': "section",
            'position': 0
        },
        'date_': {
            'selector': "span.hint.date",
            'position': 0
        },
        'title_': {
            'selector': "h3",
            'position': 0
        },
        'link_': {
            'selector': "h3 a",
            'position': 0
        },
        'image_url': {
            'selector': "img",
            'position': 0,
            'image_prefix': ''
        }
    },

    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'msc.alfaopt.com',
        'id': 8,
        'url': "https://msc.alfaopt.com/news/",
        'default_image': "https://msc.alfaopt.com/upload/CNext/2fe/2fe7acaf0ba130be140393a56efb0a50.png",
        'url_prefix': 'https://msc.alfaopt.com',
        # 'date_format': '%d-%m-%Y',
        'root_': {
            'selector': ".items.row.flexbox",
            'position': 0
        },
        'items_': {
            'selector': ".item.slice-item",
            'position': 0
        },
        'date_': {
            'selector': "span.date",
            'position': 0
        },
        'title_': {
            'selector': ".title",
            'position': 0
        },
        'link_': {
            'selector': ".title a",
            'position': 0
        },
        'image_url': {
            'selector': "img",
            'position': 0,
            'image_prefix': 'https://msc.alfaopt.com'
        }
    },

    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'aquacontrol.su',
        'id': 9,
        'url': "https://aquacontrol.su/news/",
        'default_image': "https://aquacontrol.su/UserFiles/Image/1aquacontrol.png",
        'date_format': '%d-%m-%Y',
        'url_prefix':'https://aquacontrol.su',
        'root_': {
            'selector': ".news-list",
            'position': 0
        },
        'items_': {
            'selector': "a",
            'position': 0
        },
        'date_': {
            'selector': ".panel-body code",
            'position': 0
        },
        'title_': {
            'selector': ".panel-body h3",
            'position': 0
        },
        'link_': {
            'selector': "_self_item_",
            'position': 0
        }
    },
    {
        'category': 'ОП',
        'place': 'ru',
        'name': 'teremonline.ru',
        'id': 9,
        'url': "https://www.teremonline.ru/novosti/",
        'default_image': "https://www.teremonline.ru/img/svg/logo.svg",
        'url_prefix':'https://www.teremonline.ru',
        'root_': {
            'selector': ".snp-items",
            'position': 0
        },
        'items_': {
            'selector': ".snp-itm",
            'position': 0
        },
        'date_': {
            'selector': ".snp-date",
            'position': 0
        },
        'title_': {
            'selector': ".snp-hdr",
            'position': 0
        },
        'link_': {
            'selector': ".snp-btn-wrap a",
            'position': 0
        },
        'image_url': {
            'selector': ".snp-i-bg span",
            'position': 0,
            'image_prefix': "https://www.teremonline.ru",
            "replace_before": "background-image: url(",
            "replace_after": ");"
        }
    },
# {
#         'category': 'ОП',
#         'place': 'ru',
#         'name': 'electrotest',
#         'id': 4,
#         'url': "https://www.danfoss.com/ru-ru/about-danfoss/news/?filter=news-categories%3Dpress-releases%2Csegments%3Dcf&sort=startDate_desc",
#         'root_': {
#             'selector': ".news-list-items",
#             'position': 0
#         },
#         'items_': {
#             'selector': "li.tile",
#             'position': 0
#         },
#         'date_': {
#             'selector': ".tile__text-title",
#             'position': 0
#         },
#         'title_': {
#             'selector': ".tile__text-details_item",
#             'position': 0
#         },
#         'link_': {
#             'selector': "a",
#             'position': 0
#         }
#     },
    # {
    #     # в группе PR
    #     'category': 'ОП',
    #     'place': 'ru',
    #     'name': 'ru-carel',
    #     'id': 5,
    #     'url': "https://ru-carel.com/shopnews/",
    #     'root_': {
    #         'selector': ".news__list",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': ".news__list-item",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': ".news__date",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': ".news__title-inner",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # },

    # {
    #     # В ПР
    #     'category': 'ОП',
    #     'place': 'ru',
    #     'name': 'Агава',
    #     'id': 6,
    #     'url': "https://www.kb-agava.ru/index.php?route=information/news",
    #     'root_': {
    #         'selector': "#content",
    #         'position': 0
    #     },
    #     'items_': {
    #         'selector': ".news_list_wrap",
    #         'position': 0
    #     },
    #     'date_': {
    #         'selector': ".news_date",
    #         'position': 0
    #     },
    #     'title_': {
    #         'selector': ".news_title",
    #         'position': 0
    #     },
    #     'link_': {
    #         'selector': "a",
    #         'position': 0
    #     }
    # },



]
