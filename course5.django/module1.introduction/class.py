class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def info(self):
        print("Title: {}, Author: {}, Price: {}".format(self.title, self.author, self.price))

    def apply_discount(self, discount):
        self.price = self.price * (1 - discount)

book = Book("title", "author", 100)
book.info()


jane_book = []
for book in books_data:
    if(book["author"] == "Jane Doe"):
        jane_book.append(book)

jane_book.sort(key=lambda x:x["price"])