import requests
from bs4 import BeautifulSoup
import re

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
           'accept': '*/*'}


def get_html(url, param=None):
    r = requests.get(url, headers=HEADERS, params=param)
    html = r
    return html


def define_magazine(url):
    host = url[8:]
    end_host = host.find('/')
    link = host[:end_host]
    return link


def also_number(str):
    str1 = re.findall('[0-9]', str)
    return ''.join(str1)


def parse(url):
    html = get_html(url)

    if html.status_code == 200:
        name = define_magazine(url)

        if name == 'kty.com.ua':
            price = kty_pars(html.text)
        elif name == 'aquatools.com.ua':
            price = aquatools_pars(html.text)
        elif name == '3metra.com':
            price = three_metra_pars(html.text)
        elif name == 'zaslonka.com.ua':
            price = zaslonka_pars(html.text)
        elif name == 'palladium.ua':
            price = palladim_pars(html.text)
        elif name == 'in-ua.com':
            price = install_ua(html.text)
        elif name == 'geyser.com.ua':
            price = geyser(html.text)
        elif name == 'water-pomp.com.ua':
            price = water_pomp(html.text)

        else:
            price = 'ERROR No Parser'
        print(price)
        return price
    else:
        price = 'ERROR no 200'
        print(price)
        return price


def kty_pars(html_text):
    print('[TEST] KTY начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='current-price')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def aquatools_pars(html_text):
    print('[TEST] Акватулс начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('ul', class_='list-unstyled price')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def three_metra_pars(html_text):
    print('[TEST] 3метра начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('div', class_='catalog-element-price-discount')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def zaslonka_pars(html_text):
    print('[TEST] Заслонка начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='ty-price-num')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def palladim_pars(html_text):
    print('[TEST] Паладиум начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='b')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def install_ua(html_text):
    print('[TEST] Инсталл начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('p', class_='new-price')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
    else:
        price = 'PARS ERROR'
    return price


def geyser(html_text):
    print('[TEST] Гейзер начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('div', class_='product-price__item')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def water_pomp(html_text):
    print('[TEST] Ватер начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('p', class_='b-product-cost__price')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


if __name__ == '__main__':
    test_list = [{'Название': 'Optima TPS60 Mini', 'Бренд': 'Optima',
                  'Ссылка КТУ': 'https://kty.com.ua/ru/nasosnaya-stanciya-optima-tps60-mini-037-kvt.html',
                  'Цена КТУ': None, 'Конкурент 1': 'AquaTools',
                  'Ссылка конкурента 1': 'https://aquatools.com.ua/nasosnaya-stanciya-optima-tps-60-mini.html',
                  'Цена конкурента 1': None, 'Конкурент 2': '3 метра',
                  'Ссылка конкурента 2': 'https://3metra.com/catalog/nasosnye-stantsii/nasosnaya-stantsiya-optima-tps60-mini-8400/',
                  'Цена конкурента 2': None, 'Конкурент 3': 'Заслонка',
                  'Ссылка конкурента 3': 'https://zaslonka.com.ua/nasosnaya-stanciya-optima-tps60-mini/',
                  'Цена конкурента 3': None, 'Конкурент 4': 'Гейзер',
                  'Ссылка конкурента 4': 'https://geyser.com.ua/nasosnaya-stantsiya-optima-tps60-mini/',
                  'Цена конкурента 4': None, 'Конкурент 5': 'Ватерпомп',
                  'Ссылка конкурента 5': 'https://water-pomp.com.ua/p78671483-nasosnaya-stantsiya-optima.html',
                  'Цена конкурента 5': None}, {'Название': 'Optima PC59', 'Бренд': 'Optima',
                                               'Ссылка КТУ': 'https://kty.com.ua/ru/zashhita-sukhogo-khoda-optima-pc59-c-reguliruemym-diapazonom-davleniya.html',
                                               'Цена КТУ': None, 'Конкурент 1': '3 метра',
                                               'Ссылка конкурента 1': 'https://3metra.com/catalog/avtomatika_dlya_nasosov/zashchita-sukhogo-khoda-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 1': None, 'Конкурент 2': 'Заслонка',
                                               'Ссылка конкурента 2': 'https://zaslonka.com.ua/rele-davleniya-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 2': None, 'Конкурент 3': None,
                                               'Ссылка конкурента 3': None, 'Цена конкурента 3': None,
                                               'Конкурент 4': None, 'Ссылка конкурента 4': None,
                                               'Цена конкурента 4': None, 'Конкурент 5': None,
                                               'Ссылка конкурента 5': None, 'Цена конкурента 5': None}]

    for i in test_list:
        if i['Ссылка КТУ']:
            price = parse(i['Ссылка КТУ'])
            i['Цена КТУ'] = price

        if i['Ссылка конкурента 1']:
            price = parse(i['Ссылка конкурента 1'])
            i['Цена конкурента 1'] = price

        if i['Ссылка конкурента 2']:
            price = parse(i['Ссылка конкурента 2'])
            i['Цена конкурента 2'] = price

        if i['Ссылка конкурента 3']:
            price = parse(i['Ссылка конкурента 3'])
            i['Цена конкурента 3'] = price

        if i['Ссылка конкурента 4']:
            price = parse(i['Ссылка конкурента 4'])
            i['Цена конкурента 4'] = price

        if i['Ссылка конкурента 5']:
            price = parse(i['Ссылка конкурента 5'])
            i['Цена конкурента 5'] = price

    print(test_list)
