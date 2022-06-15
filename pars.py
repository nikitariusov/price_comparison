'''Принцип добавления новых интернет магазинов:
1. Добавляем ссылку в кортеж added_magazine
2. Пишем функцию название магазина-pars, в офсновном копируем с другого магазина но указываем элементы для поиска на странице
3. В def parse пишем условие и указываем созданную функцию
4. Если ссылка не работает через request то открываем через def open_in_webdriver (Селениум)
5. В def open_in_webdriver пишем условие на новый магазин по примеру КранОк'''

import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from typing import Union

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
           'accept': '*/*'}

added_magazine = ('kty.com.ua', 'aquatools.com.ua', '3metra.com', 'zaslonka.com.ua', 'palladium.ua', 'in-ua.com',
                  'in-ua.com', 'geyser.com.ua', 'water-pomp.com.ua', 'bt.rozetka.com.ua', 'rozetka.com.ua',
                  'kranok.ua')


def get_html(url, param=None):
    r = requests.get(url, headers=HEADERS, params=param)
    html = r
    return html


def open_in_webdriver(url: str, name: str) -> int | str:  # str возвращаем только в виде ошибок, цены - только int
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    if name == 'kranok.ua':
        try:
            '''Поиск обычнной цены'''
            WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'product-right')))
            try:
                price = driver.find_element(by=By.CLASS_NAME, value='normal-price').find_element(by=By.CLASS_NAME,
                                                                                                 value='price').text
            except:
                price = None

            if not price:
                try:
                    price = driver.find_element(by=By.CLASS_NAME, value='sale-price').find_element(by=By.ID,
                                                                                                   value='sale-price').text
                except:
                    price = None

            if not price:
                price = driver.find_element(by=By.CLASS_NAME, value='stock-no').text
                if price == 'Переглянути подібні товари':
                    price = 'Нет в наличии/нет цены'
                else:
                    price = 'что-то пошло не так'

            if price != 'Нет в наличии/нет цены' and price:
                price = int(also_number(price))
            return price
        except TimeoutException:
            price = 'Страница не загрузилась'
            return price

    else:
        price = 'Need Selenium Parser'

        driver.quit()
        return price


def define_magazine(url):
    host = url[8:]
    end_host = host.find('/')
    link = host[:end_host]
    return link


def also_number(str):
    str = str[:str.find(',')]
    str1 = re.findall('\d', str)
    return ''.join(str1)


def parse(url: str) -> str | int:  # str возвращаем только в виде ошибок, цены - только int
    name = define_magazine(url)
    if name in added_magazine:
        html = get_html(url)
        if html.status_code == 200:
            if name == 'kty.com.ua':
                try:
                    price = int(kty_pars(html.text))
                except ValueError:
                    price = kty_pars(html.text)

            elif name == 'bt.rozetka.com.ua' or name == 'rozetka.com.ua':
                try:
                    price = int(rozetka_pars(html.text))
                except ValueError:
                    price = rozetka_pars(html.text)

            elif name == 'kranok.ua':
                try:
                    price = int(kranok_pars(html.text))
                except ValueError:
                    price = kranok_pars(html.text)

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
                price = '2 No Parser'
            return price

        elif html.status_code == 403:
            try:
                price = open_in_webdriver(url, name)
            except:
                price = 'Selenium ERROR'

        else:
            price = 'No 200'
            return price
    else:
        price = 'No Parser'
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


def kranok_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('span', class_='price')
    if item:
        price = item.text
        price = also_number(price)
    else:
        price = 'PARS ERROR'
    return price


def rozetka_pars(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    item = soup.find('p', class_='product-prices__big')
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


if __name__ == '__main__':
    url = 'https://water-pomp.com.ua/p1274949942-mylnitsa-globus-lux.html'
    price = parse(url)
    print(f'Тип значения price {type(price)}')
    print(f'Цена: {price}')
