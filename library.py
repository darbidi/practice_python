class Book:
    def __init__(self,title,author,book_id,is_available=True):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = is_available
class Person:
    def __init__(self,name):
        self.name = name
class Member(Person):
    def  __init__(self,member_id,name):
      self.member_id = member_id
      self.borrowed_books=[]
      super().__init__(name)
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    def add_book(self,book):
       self.books.append(book)
    def add_member(self,member):
        self.members.append(member)
    def find_book(self,book_id):
         for book in self.books:
             if book.book_id == book_id:
                 return book
         return None
    def find_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None
    def borrow_book(self,book_id,member_id):
        book = self.find_book(book_id)
        member=self.find_member(member_id)

        if book==None or member==None:
            print("خطا: کتاب یا عضو در سیستم پیدا نشد!")
            return
        if book.is_available ==True:
           book.is_available=False
           member.borrowed_books.append(book)
           print("کتاب با موفقیت امانت داده شد")


my_lib = Library()
book1= Book ("پایتون","گیدو",101)
member1=Member(100,"فاطمه")
my_lib.add_book(book1)
my_lib.add_member(member1)
my_lib.borrow_book(101, 100)

print("آیا کتاب پایتون موجود است؟", book1.is_available)


