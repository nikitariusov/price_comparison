import openpyxl
from datetime import datetime, date
from colorama import init, Fore


def try_save(sheet, i, j, cols_name, price):
    try:
        if i[price]:
            sheet[f'{cols_name}{j}'] = i[price]
    except KeyError:
        pass


def save_file(data, file):
    wb = openpyxl.load_workbook(filename=file)
    sheet = wb.active

    j = 2
    for i in data:
        try_save(sheet, i, j, 'D', 'Цена КТУ')
        try_save(sheet, i, j, 'G', 'Цена конкурента 1')
        try_save(sheet, i, j, 'J', 'Цена конкурента 2')
        try_save(sheet, i, j, 'M', 'Цена конкурента 3')
        try_save(sheet, i, j, 'P', 'Цена конкурента 4')
        try_save(sheet, i, j, 'S', 'Цена конкурента 5')
        j += 1

    filename = f'Проверен-{date.today()}.xlsx'
    wb.save(filename)

    init(autoreset=True)  # запускаем колораму
    print(Fore.GREEN + f'''[INFO]\tCохранен файл {filename}''')
    print('''\nВыход - Enter''')


if __name__ == '__main__':
    print(date.today())
    init(autoreset=True)
    print(Fore.GREEN + f'''[INFO]\tCохранен файл ''')
    print('''\nВыход - Enter''')
