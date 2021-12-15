
from dogs.dog import Dog


class Sheperd(Dog):
    def __init__(self, name: str, price: int):
        Dog.__init__(self)
        self.name = name
        self.price = price

    @property
    def details(self):
        print("{} ---- {}".format(self.name, self.price))
