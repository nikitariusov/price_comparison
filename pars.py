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
            try:
                price = int(kty_pars(html.text))
            except ValueError:
                price = kty_pars(html.text)

        elif name == 'aquatools.com.ua':
            try:
                price = int(aquatools_pars(html.text))
            except ValueError:
                price = aquatools_pars(html.text)

        elif name == '3metra.com':
            try:
                price = int(three_metra_pars(html.text))
            except ValueError:
                price = aquatools_pars(html.text)

        elif name == 'zaslonka.com.ua':
            try:
                price = int(zaslonka_pars(html.text))
            except ValueError:
                price = zaslonka_pars(html.text)

        elif name == 'palladium.ua':
            try:
                price = int(palladim_pars(html.text))
            except ValueError:
                price = palladim_pars(html.text)

        elif name == 'in-ua.com':
            try:
                price = int(install_ua(html.text))
            except ValueError:
                price = install_ua(html.text)

        elif name == 'geyser.com.ua':
            try:
                price = int(geyser(html.text))
            except ValueError:
                price = geyser(html.text)

        elif name == 'water-pomp.com.ua':
            try:
                price = int(water_pomp(html.text))
            except ValueError:
                price = water_pomp(html.text)

        else:
            price = 'ERROR No Parser'
        return price
    else:
        price = 'ERROR no 200'
        return price


def kty_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='current-price')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def aquatools_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('ul', class_='list-unstyled price')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def three_metra_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('div', class_='catalog-element-price-discount')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def zaslonka_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='ty-price-num')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def palladim_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='b')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def install_ua(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('p', class_='new-price')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def geyser(html_text):
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
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('p', class_='b-product-cost__price')
    if item:
        price = item.text
        price = price[:price.find('.')].strip()
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price
