import sqlite3
class Product:
    def __init__(self,product_id,name,price,category):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.category=category


class ShoppingCart:
    def __init__(self):
        self.products={}
    def add_product(self, product,quantity):
        if product in self.products:
            self.products[product] += quantity
        else:
            self.products[product] = quantity

class Person:
     def __init__(self,name):
         self.name=name




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
store_inventory = Inventory()
class Customer(Person):
    def __init__(self,name,customer_id):
        self.customer_id=customer_id
        super().__init__(name)
        self.cart=ShoppingCart()
    def checkout(self,store_inventory):
       for product,quantity in self.cart.products.items():
           store_inventory.reduce_stock(product,quantity)
       self.cart.products = {}

       print(f"خرید مشتری {self.name} نهایی شد!")




# --- بخش اجرای تستی ---
# ۱. انبار دیجی‌کالا رو می‌سازیم و جنس توش می‌ریزیم
digikala = Inventory()
digikala.add_new_stock("لپ‌تاپ", 5)
digikala.add_new_stock("موس", 10)
print("موجودی اول صبح:", digikala.stocks)

# ۲. مشتری وارد میشه
ali = Customer("علی", "C-123")

# ۳. علی خریدهاش رو میریزه تو سبد
ali.cart.add_product("لپ‌تاپ", 2)
ali.cart.add_product("موس", 15) # عمداً بیشتر از موجودی می‌خوایم!

# ۴. رفتن پای صندوق
print("\n--- در حال پردازش ---")
ali.checkout(digikala)
print("موجودی آخر شب:", digikala.stocks)



