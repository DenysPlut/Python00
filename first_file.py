#TODO: basic class

class Book():
    def __init__(self, title, author, pages, price):
         self.title = title
        #TODO: properties
         self.author = author
         self.pages = pages
         self.price = price

    #TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount



#TODO: an instance of the class
book1 = Book("Twenty Thousand Leagues Under the Seas", "Jules Verne", 1100, 35.70)
book2 = Book("Critique of Judgement", "Emmanuel Kant", 567, 27)

#TODO: the print and class property

print(book1.getprice())

#TODO: setting the discount

print(book2.getprice())
book2.setdiscount(0.25)
print(book2.getprice())

