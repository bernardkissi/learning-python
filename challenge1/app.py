
from atm import ATM
from bank import Bank
from customer import Customer

# creating customers
account1 = Customer("bernard", "kissi", "santasi", 108844567, "bern@gmail.com")
account2 = Customer("Austin", "Boateng", "Atonsu", 108844565, "bern@gmail.com")
account3 = Customer("Theo", "Asamoah", "Oforikrom", 108844235, "thro@gmail.com")
account3.getDetails()
# Creating a bank
# Adding customers to the bank
Ecobank = Bank("Ecobank")
Ecobank.addAccounts(account1, account2, account3)
print('{} accounts created in {}'.format(Ecobank.totalAccounts, Ecobank.name))

# ATM machine
# create the ATM machine for the bank
EcobankATM = ATM(Ecobank)
# Fetch account by account number from user
ATMCard = input("Please insert your ATMCard number: ")
# intialize the ATM machine
ATMachine = EcobankATM.initialize(ATMCard)

if ATMachine is not None:
    while ATMachine.isActive:
        option = input("Please select an option: ")
        ATMachine.run(option)
else:
    ATM.initializationFailed()
