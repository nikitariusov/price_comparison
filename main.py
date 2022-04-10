from read import read_file

file = 'test/prods.xlsx'

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


if __name__ == '__main__':
    print(read_file(file))
