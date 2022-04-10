file = 'test/prods.xlsx'

class Product:

    def __init__(self, name, kty_link, competitor_1, competitor__link_1,
                 competitor_2, competitor__link_2, competitor_3, competitor__link_3,):
        self.name = name
        self.kty_link = kty_link
        self.competitor_1 = competitor_1
        self.competitor_link_1 = competitor__link_1
        self.competitor_2 = competitor_2
        self.competitor_link_2 = competitor__link_2
        self.competitor_3 = competitor_3
        self.competitor_link_3 = competitor__link_3
        self.kty_price = None
        self.competitor_1_price = None
        self.competitor_2_price = None
        self.competitor_3_price = None

