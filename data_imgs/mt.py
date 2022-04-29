data = [
      {
          'category': 'Meyertec',
          'place': 'com',
          'id': '0',
          'name': 'Rittal',
          'url': "https://www.rittal.com/ru-ru/content/ru/unternehmen/presse/pressemeldungen/pressemeldungen.jsp",
          'default_image': "https://www.rittal.com/ru-ru/content/media/layout/logos/logo_rittal.png",
          'url_prefix': 'https://www.rittal.com/ru-ru/content/ru/unternehmen/presse/pressemeldungen/',
          'root_': {
              'selector': "div.cnt-inner",
              'position': 0
          },
          'items_': {
              'selector': "ul.teaserlist-press",
              'position': 0
          },
          'date_': {
              'selector': "",
              'position': 0
          },
          'title_': {
              'selector': "a.moredirect",
              'position': 0
          },
          'link_': {
              'selector': "a.moredirect",
              'position': 0
          },
          'image_url': {
              'selector': "img",
              'position': 0,
              'image_prefix': ""
          }
      },
      {
          'category': 'Meyertec',
          'place': 'com',
          'id': '1',
          'name': 'Pfannenberg',
          'url': "https://www.pfannenberg.com/ru/novosti-pressa/novosti-i-press-relizy/dateFilter/2022/",
          'default_image': "https://www.pfannenberg.com/typo3conf/ext/hn_pfannenberg/Resources/Public/Images/Pfannenberg_Logo_RU_RGB.svg",
          'url_prefix': 'https://www.pfannenberg.com',
          'root_': {
              'selector': "div.bordered-list",
              'position': 0
          },
          'items_': {
              'selector': "div.teaser-article-wrap",
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
              'selector': "div.teaser-footer > a",
              'position': 0
          },
          'image_url': {
              'selector': 'img',
              'position': 0,
              'image_prefix': 'https://www.pfannenberg.com'
          }
      },
      {
          'category': 'Meyertec',
          'place': 'ru',
          'id': '2',
          'name': 'DKC',
          'url': "https://www.dkc.ru/ru/about/news/",
          'default_image': "https://www.dkc.ru/upload/iblock/cb2/cb24b03c7e286a3b27b45d1eafb0e972.jpg",
          'url_prefix': 'https://www.dkc.ru',
          'root_': {
              'selector': "div.news",
              'position': 0
          },
          'items_': {
              'selector': "div.news__item",
              'position': 0
          },
          'date_': {
              'selector': "span",
              'position': 0
          },
          'title_': {
              'selector': "a.news__itemLink",
              'position': 0
          },
          'link_': {
              'selector': "a",
              'position': 0
          },
          'image_url': {
              'selector': 'img.news__itemImage',
              'position': 0,
              'image_prefix': 'https://www.dkc.ru'
          }
      },
      {
          'category': 'Meyertec',
          'place': 'ru',
          'id': '3',
          'name': 'DEKraft',
          'url': "https://www.dek.ru/news.htm",
          'default_image': "https://www.dek.ru/images/logo.svg",
          'url_prefix': 'https://www.dek.ru/',
          'root_': {
              'selector': "div.news_list",
              'position': 0
          },
          'items_': {
              'selector': "div.item",
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
          'category': 'Meyertec',
          'place': 'ru',
          'id': '4',
          'name': 'TDM ELECTRIC',
          'url': "https://tdme.ru/news/2022/",
          'default_image': "https://tdme.ru/_img/LogoR.png",
          'url_prefix': 'https://tdme.ru',
          # 'date_format': '',
          'root_': {
              'selector': "ul.news",
              'position': 0
          },
          'items_': {
              'selector': "ul.news > li",
              'position': 0
          },
          'date_': {
              'selector': "h3",
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
          'category': 'Meyertec',
          'place': 'ru',
          'id': '5',
          'name': 'Провенто',
          'url': "https://provento-electro.ru/about/news/",
          'default_image': "https://provento-electro.ru/images/logo.png",
          'url_prefix': 'https://provento-electro.ru',
          'date_format':'%d.%m.%Y',
          'root_': {
              'selector': "ul.obj-news__list",
              'position': 0
          },
          'items_': {
              'selector': "li.obj-news__item",
              'position': 0
          },
          'date_': {
              'selector': "span",
              'position': 0
          },
          'title_': {
              'selector': "h2",
              'position': 0
          },
          'link_': {
              'selector': "a.obj-news__content",
              'position': 0
          }
      },
      {
          'category': 'Meyertec',
          'place': 'ru',
          'id': '6',
          'name': 'Pizzato',
          'url': "https://pizzato.su/novosti.html",
          'default_image': "https://pizzato.su/images/logos/53/logo.png",
          'root_': {
              'selector': "div.ty-pagination-container",
              'position': 0
          },
          'items_': {
              'selector': "div.ty-blog__item",
              'position': 0
          },
          'date_': {
              'selector': "div.ty-blog__date",
              'position': 0
          },
          'title_': {
              'selector': "h2",
              'position': 0
          },
          'link_': {
              'selector': "a.ty-btn__secondary",
              'position': 0
          },
          'image_url': {
              'selector': 'img',
              'position': 0,
              'image_prefix': ''
          }
      },
      {
          'category': 'Meyertec',
          'place': 'else',
          'id': '7',
          'name': 'KLEMSAN',
          'url': "https://klemsan.com.tr/news-russia",
          'default_image': "https://klemsan.com.tr/Images/logo.png",
          'url_prefix': 'https://klemsan.com.tr',
          'root_': {
              'selector': "ul.support-items",
              'position': 0
          },
          'items_': {
              'selector': "ul.support-items > li",
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
      {
          'category': 'Meyertec',
          'place': 'ru',
          'id': '8',
          'name': 'Tekfor',
          'url': "http://www.tekfor.ru/info/news/",
          'default_image': "http://www.tekfor.ru/bitrix/templates/aspro-allcorp/images/tekfor_logo_2011.svg",
          'url_prefix': 'http://www.tekfor.ru',
          'root_': {
              'selector': "div.group-content",
              'position': 0
          },
          'items_': {
              'selector': "div.wdate",
              'position': 0
          },
          'date_': {
              'selector': "div.text > div.period",
              'position': 0
          },
          'title_': {
              'selector': "div.text > div.title",
              'position': 0
          },
          'link_': {
              'selector': "div.text > a",
              'position': 0
          },
          'image_url': {
              'selector': 'img',
              'position': 0,
              'image_prefix': 'http://www.tekfor.ru'
          }
      },
      {
          'category': 'Meyertec',
          'place': 'ru',
          'id': '9',
          'name': 'Briswik',
          'url': "https://briswik.ru/category/novosti-i-stati/",
          'default_image': "https://briswik.ru/wp-content/uploads/cropped-logo-1980x674.png",
          'url_prefix': '',
          'root_': {
              'selector': "main#site-content",
              'position': 0
          },
          'items_': {
              'selector': "article.category-novosti-i-stati",
              'position': 0
          },
          'date_': {
              'selector': "",
              'position': 0
          },
          'title_': {
              'selector': "div.entry-title",
              'position': 0
          },
          'link_': {
              'selector': "div.entry-title > a",
              'position': 0
          },
          'image_url': {
              'selector': 'img',
              'position': 0,
              'image_prefix': ''
          }
      },
#     ua
    {
        'category': 'Meyertec',
        'dop_cat': ['Meyertec'],
        'place': 'ua',
        'id': '6',
        'name': 'АСКО',
        'url': "https://www.acko.ua/news/",
        'url_prefix': '',
        'date_format': '%d.%m.%Y',
        'default_image': 'https://www.acko.ua/local/templates/new_asko_index/foto/foto-site/logo.svg',
        'root_': {
            'selector': "section.news-catalog",
            'position': 0
        },
        'items_': {
            'selector': "div.news-catalog_it",
            'position': 0
        },
        'date_': {
            'selector': "span",
            'position': 0
        },
        'title_': {
            'selector': "p",
            'position': 0
        },
        'link_': {
            'selector': "a",
            'position': 0
        },
          'image_url': {
              'selector': 'div.news-catalog_it--foto',
              'position': 0,
              'image_prefix': 'https://www.acko.ua',
              'replace_before': 'background-image:url("',
              'replace_after': '");'
          }
    },
#     other
    {
        'category': 'Meyertec',
        'dop_cat': ['Meyertec'],
        'place': 'else',
        'id': '0',
        'name': 'Werma',
        'url': "https://www.werma.com/en/news/news.php",
        'default_image': "https://www.werma.com/gfx/werma_logo.png",
        'url_prefix': 'https://www.werma.com',
        'root_': {
            'selector': "div.news",
            'position': 0
        },
        'items_': {
            'selector': "div.news > div.col-md-6",
            'position': 0
        },
        'date_': False,
        'title_': {
            'selector': "h3",
            'position': 0
        },
        'link_': {
            'selector': "a.more",
            'position': 0
        },
        'image_url': {
            'selector': "div.img",
            'position': 0,
            'image_prefix': 'https://www.werma.com'
        }
    }
]
