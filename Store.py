class Product:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category

class Person():
     def __init__(self,name):
         self.name=name


class Customer(Person):
    def __init__(self,name,customer_id):
        self.customer_id=customer_id

        super().__init__(name)

class Vendor(Person):
    def __init__(self,name,vendor_id):
        self.Vendor_id=vendor_id
        super().__init__(name)

class Inventory:
    def __init__(self):
        self.stocks = {}
    def add_new_stock(self, product, quantity):
        if product in self.stocks:
            self.stocks[product] += quantity
        else:
            self.stocks[product] = quantity

    def reduce_stock(self, product, quantity):
        # شرط امنیتی انبار رو اینجا کامل کن:
        if  product in self.stocks and self.stocks[product] >= quantity:
            self.stocks[product] -= quantity
            print(f"{quantity} تا از محصول کم شد.")
        else:
            print("خطا: موجودی انبار برای این درخواست کافی نیست!")






