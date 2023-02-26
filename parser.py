import requests
from bs4 import BeautifulSoup as bs4
import csv

HOST = 'https://jut.su/'
URL = 'https://jut.su/kimetsu-yaiba/?yrwinfo=1677256495311481-9618476846770718249-vla1-3228-vla-l7-balancer-8080-BAL-1242'

HEADERS = {
    'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, * / *;q = 0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
    }

def get_html(url, params=''):
    """Функция получает html страницу """
    r = requests.get(url, headers=HEADERS, params=params)
    return r
html = get_html(URL)
print(html)

def get_content(html):
    # Получаем объект страницы, и к парсеру обращаемся
    soup = bs4(html, 'html.parser')
    #Получаем элементы
    items = soup.find_all('div', class_='content')
    #Складываем элементы
    cards=[]

    for item in items:
        cards.append(
            {   #Удалить лишние пробелы strip=True
                'title':item.find('div', class_='the_invis').get_text(strip=True),
                #Ищем ссылку и получаем содержимое ссылки (href)
                #Чтобы перейти по ссылке вставляем HOST + item.find()
                'series': HOST + item.find('div', class_='').find('a').get('href'),
                'description': item.find('p', class_='under_video uv_rounded_bottom the_hildi').get_text(strip=True),
                'photo': item.find('div', class_='all_anime_title').get('src'),
            }
        )
    return cards
#Проверка
html = get_html(URL)
print(get_content(html.text))

def parser():
    #PAGINATION проход страниц
    PAGINATION = int(input("Укажите кол-во страниц для парсинга: ").strip())

    html = get_html(URL)
    #Проверка кода ответа статуса сайта
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION):
            print(f"Парсинг страницы: {page}")
            html = get_html(URL, params={'page':page})
            cards.extend(get_content(html.text))
        print(cards)
    else:
        print('Error')
parser()

