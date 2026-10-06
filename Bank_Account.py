class Account():
    def __init__(self,account_number,open_date,balance):
        self.account_number=account_number
        self.open_date=open_date
        self.balance=balance
    def deposit(self,deposit_amount):
        self.balance=self.balance + deposit_amount
    def withdraw(self,withdraw_amount):
        self.balance=self.balance - withdraw_amount

class person():
    def __init__(self,name,national_code,password):
        self.name=name
        self.national_code=national_code
        self.password=password

class user(person):
    def __init__(self,user_id,name,national_code,password):
        self.user_id=user_id
        super().__init__(name,national_code,password)

class customer(person):
    def __init__(self,customer_id,name,national_code,password):
        self.customer_id=customer_id
        self.accounts = []
        super().__init__(name,national_code,password)
    def add_account(self,account_obj):
        self.accounts.append(account_obj)


customer_1=customer(1,"customer1","123456","123456")
acc1=Account(1,"1404/04/01",123456)
customer_1.add_account(acc1)

# بعد از اینکه مشتری و حساب رو ساختی و به هم وصل کردی:

# دست کردن تو کیف مشتری و برداشتنِ اولین حساب (ایندکس 0 در لیست)
first_account = customer_1.accounts[0]

# حالا با متد deposit پولی رو به این حساب واریز کن
first_account.deposit(500)

# در نهایت موجودی رو پرینت بگیر
print("موجودی جدید:", first_account.balance)

first_account.withdraw(500)
print("موجودی جدید:", first_account.balance)