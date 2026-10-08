class Product:
    def __init__(self,name,price,stock,category):
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category

class person():
     def __init__(self,name):
         self.name=name


class Customer(person):
    def __init__(self,name,customer_id):
        self.customer_id=customer_id
        super().__init__(name)

class Vendor(person):
    def __init__(self,name,Vendor_id):
        self.Vendor_id=Vendor_id
        super().__init__(name)




