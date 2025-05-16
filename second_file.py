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

#TODO: compare two types together
print(type(b1) == type(b2))
print(type(b1) == type(n2))

#TODO: use isinstance to compare a specific instance to a known type
# print(isinstance(b1, Book))
# print(isinstance(n1, Newspaper))
# print(isinstance(b1, Newspaper))
print(isinstance(n2, object))



