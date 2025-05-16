class Book():
    def __init__(self, title):
         self.title = title

class Newspaper():
    def __init__(self, name):
         self.name = name


# create some instance of the classes

b1 = Book("Catcher in the Rye")
b2 = Book("Harry Potter")
n1 = Newspaper("Der Spiegel")
n2 = Newspaper("Das Bild")

# TODO: use type() to create object type
print(type(b1))
print(type(n1))

