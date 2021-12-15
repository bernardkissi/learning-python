from dogs.dog import Dog


class Store:
    def __init__(self, name: str, dogs: list = []):
        self.name = name
        self.dogs = dogs

    def addDogs(self, *dogs: 'Dog'):
        for dog in dogs:
            self.dogs.append(dog)

    def fetchDogs(self):
        print("***********************************************")
        print("Available dogs we have in {}".format(self.name))
        print("**********************************************")
        for dog in self.dogs:
            print("{} ------------ {}\n".format(dog.name, dog.price))

    def fetchDog(self, name: str):
        for dog in self.dogs:
            if dog.name == str(name):
                return dog.details
        print("The dog name {} cannot be found".format(name))
