from read import read_file
from pars import *
from save import save_file
import easygui
from colorama import init, Fore

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
    - rozetka.com.ua
    - kranok.ua
    
    Для работы необходим файл формата .xlsx с определенным расположением столбцов.
    После проверки будет сохранен новый файл с отчетом.
    
    
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
    j = 1
    for i in data:
        print(f'Парсинг {j} из {products_count} товаров...')
        start_pars(i, 'Ссылка КТУ', 'Цена КТУ')
        start_pars(i, 'Ссылка конкурента 1', 'Цена конкурента 1')
        start_pars(i, 'Ссылка конкурента 2', 'Цена конкурента 2')
        start_pars(i, 'Ссылка конкурента 3', 'Цена конкурента 3')
        start_pars(i, 'Ссылка конкурента 4', 'Цена конкурента 4')
        start_pars(i, 'Ссылка конкурента 5', 'Цена конкурента 5')
        j += 1
    return data


def check_file(file):
    format_file = file[file.find('.'):]
    return format_file


if __name__ == '__main__':
    init(autoreset=True)
    print(message)
    # input()
    try:
        file = easygui.fileopenbox('Выберите файл')
        while check_file(file) != '.xlsx':
            print(Fore . YELLOW + 'Выберите файл Excel!')
            file = easygui.fileopenbox('Выберите файл')
        data = read_file(file)
        products_count = len(data)
        print(Fore . BLUE + f'[INFO] Общее кол-во товаров: {products_count}.')
        base = cell_parsing(data)
        save_file(base, file)
        input()
    except TypeError:
        print(Fore . RED + error_choise_file)
        input()
        exit()
