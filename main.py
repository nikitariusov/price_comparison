from read import read_file
from pars import *
from save import save_file
import easygui


# class Product:
#
#     def __init__(self, name, kty_link, kty_price,
#                  competitor_1, competitor__link_1, competitor_1_price,
#                  competitor_2, competitor__link_2, competitor_2_price,
#                  competitor_3, competitor__link_3, competitor_3_price):
#         self.name = name
#         self.kty_link = kty_link
#         self.kty_price = kty_price
#         self.competitor_1 = competitor_1
#         self.competitor_link_1 = competitor__link_1
#         self.competitor_1_price = competitor_1_price
#         self.competitor_2 = competitor_2
#         self.competitor_link_2 = competitor__link_2
#         self.competitor_2_price = competitor_2_price
#         self.competitor_3 = competitor_3
#         self.competitor_link_3 = competitor__link_3
#         self.competitor_3_price = competitor_3_price

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
    file = easygui.fileopenbox('Выберите файл')
    data = read_file(file)
    print(data)
    base = cell_parsing(data)
    print(base)
    save_file(base, file)
