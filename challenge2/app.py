from dogs.bulldog import Bulldog
from dogs.sheperd import Sheperd
from store import Store

# creating dogs
dog1 = Bulldog("bulldog-puppy", 500)
dog2 = Bulldog("bulldog-male", 1500)
dog3 = Bulldog("bulldog-female", 3000)
dog4 = Sheperd("german-sheperd", 1000)
dog5 = Sheperd("german-sheperd-puppy", 1300)
dog6 = Sheperd("russian-german-shepered", 2100)
dog7 = Sheperd("austrian-german-sheperd", 2500)

# creating a petstore
petStore = Store("MATT PET STORE")
petStore.addDogs(dog1, dog2, dog3, dog4, dog5, dog6, dog7)

# show all dogs in store
petStore.fetchDogs()

# search for the customers prefered dog
selected = str(input("Enter the name of the dog you want to purchase: "))
petStore.fetchDog(selected)

# customer can own a dog or dogs


# customer plays with his/her purchased dog
