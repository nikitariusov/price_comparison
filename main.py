from read import read_file
from pars import *

file = 'test/prods2.xlsx'


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

def cell_parsing(data):
    for i in data:
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
    return data


if __name__ == '__main__':
    data = read_file(file)
    base = cell_parsing(data)
    print(base)
