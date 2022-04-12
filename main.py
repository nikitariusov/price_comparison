from read import read_file
from pars import *
from save import save_file
import easygui


message = '''Программа для мониторинга цен на интернет ресурсах.

    !!! Любое копирование кода или распространение программы будет считаться нарушением авторских прав !!!

Доступные ресурсы:
    - kty.com.ua
    - aquatools.com.ua
    - 3metra.com
    - zaslonka.com.ua
    - palladium.ua
    - in-ua.com
    - geyser.com.ua
    - water-pomp.com.ua
    
    Для работы необходим файл формата .xlsx с определенным расположением столбцов.
    После проверки будет сохранен новый файл с отчетом.
    
    Контакт для связи: telegram @n_konstruktor
    
    START - Enter
    '''

error_choise_file = '''     ERROR ошибка выбора файла

    Выход - Enter'''

def start_pars(i, link_name_cell, price_name_cell):
    try:
        if i[link_name_cell]:
            price = parse(i[link_name_cell])
            i[price_name_cell] = price
    except KeyError:
        pass


def cell_parsing(data):
    for i in data:
        start_pars(i, 'Ссылка КТУ', 'Цена КТУ')
        start_pars(i, 'Ссылка конкурента 1', 'Цена конкурента 1')
        start_pars(i, 'Ссылка конкурента 2', 'Цена конкурента 2')
        start_pars(i, 'Ссылка конкурента 3', 'Цена конкурента 3')
        start_pars(i, 'Ссылка конкурента 4', 'Цена конкурента 4')
        start_pars(i, 'Ссылка конкурента 5', 'Цена конкурента 5')
    return data


if __name__ == '__main__':
    print(message)
    x = str(input())
    try:
        file = easygui.fileopenbox('Выберите файл')
        data = read_file(file)
        products_count = len(data)
        print(f'[INFO] Общее кол-во товаров: {products_count}.')
        base = cell_parsing(data)
        save_file(base, file)
    except TypeError:
        print(error_choise_file)
        input()
        exit()
