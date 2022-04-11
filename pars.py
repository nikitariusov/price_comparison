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
            kty_pars(html.text)
        elif name == 'aquatools.com.ua':
            aquatools_pars(html.text)
        elif name == '3metra.com':
            three_metra_pars(html.text)
        elif name == 'zaslonka.com.ua':
            zaslonka_pars(html.text)


def kty_pars(html_text):
    print('[TEST] KTY начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    price = soup.find('span', class_='current-price').text
    price = also_number(price)
    print(price)


def aquatools_pars(html_text):
    print('[TEST] Акватулс начало парсинга')
    soup = BeautifulSoup(html_text, 'html.parser')
    price = soup.find('ul', class_='list-unstyled price').text
    price = also_number(price)
    print(price)

def three_metra_pars(html_text):
    print('[TEST] 3метра начало парсинга')


def zaslonka_pars(html_text):
    print('[TEST] Заслонка начало парсинга')





if __name__ == '__main__':
    test_list = [{'Название': 'Насосная станция Optima TPS60 Mini', 'Бренд': 'Optima',
                  'Ссылка КТУ': 'https://kty.com.ua/ru/nasosnaya-stanciya-optima-tps60-mini-037-kvt.html',
                  'Цена КТУ': None, 'Конкурент 1': 'AquaTools',
                  'Ссылка конкурента 1': 'https://aquatools.com.ua/nasosnaya-stanciya-optima-tps-60-mini.html',
                  'Цена конкурента 1': None, 'Конкурент 2': '3 метра',
                  'Ссылка конкурента 2': 'https://3metra.com/catalog/nasosnye-stantsii/nasosnaya-stantsiya-optima-tps60-mini-8400/',
                  'Цена конкурента 2': None, 'Конкурент 3': 'Заслонка',
                  'Ссылка конкурента 3': 'https://zaslonka.com.ua/nasosnaya-stanciya-optima-tps60-mini/',
                  'Цена конкурента 3': None}, {'Название': 'Optima PC59', 'Бренд': 'Optima',
                                               'Ссылка КТУ': 'https://kty.com.ua/ru/zashhita-sukhogo-khoda-optima-pc59-c-reguliruemym-diapazonom-davleniya.html',
                                               'Цена КТУ': None, 'Конкурент 1': '3 метра',
                                               'Ссылка конкурента 1': 'https://3metra.com/catalog/avtomatika_dlya_nasosov/zashchita-sukhogo-khoda-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 1': None, 'Конкурент 2': 'Заслонка',
                                               'Ссылка конкурента 2': 'https://zaslonka.com.ua/rele-davleniya-optima-pc59-n-c-reguliruemym-diapazonom-davleniya/',
                                               'Цена конкурента 2': None, 'Конкурент 3': None,
                                               'Ссылка конкурента 3': None, 'Цена конкурента 3': None}]

    for i in test_list:
        if i['Ссылка КТУ']:
            parse(i['Ссылка КТУ'])
        if i['Ссылка конкурента 1']:
            parse(i['Ссылка конкурента 1'])
        if i['Ссылка конкурента 2']:
            parse(i['Ссылка конкурента 2'])
        if i['Ссылка конкурента 3']:
            parse(i['Ссылка конкурента 3'])
