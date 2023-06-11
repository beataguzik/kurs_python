"""Utwórz klasę sklep. Sklep posiada różne produkty.
 W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic."""



class Shop:



    def __init__(self):
        self.products = ['koszulka', 'kurtka', 'spodnie', 'buty']

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def see_products(self):
        if not self.products:
            print(f'Brak tego produktu w sklepie.')
        else:
            print('Dostępne produkty w sklepie:')
            for product in self.products:
                print(product)

    def put_on_product(self, product):
        if product in self.products:
            print(f'Przymierzono produkt: {product}')
        else:
            print(f'Produkt {product} nie jest dostępny w sklepie.')

    def buy(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f'Kupiono : {product}')
        else:
            print(f'Produkt {product}  jest nie dostępny w sklepie.')

    def return_product(self, product):
        self.products.append(product)
        print(f'Zwrócono : {product}')




shop = Shop()


# shop.add_product('koszulka')
# shop.add_product('kurtka')
# shop.add_product('spodnie')
# shop.add_product('buty')

shop.see_products()

shop.put_on_product('koszulka')
shop.put_on_product('kurtka')

shop.buy('spodnie')
shop.see_products()
shop.return_product('spodnie')
shop.see_products()

