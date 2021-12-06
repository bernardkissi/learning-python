from challenge1.bank import Bank
from customer import Customer


class ATM:

    isActive = True

    def __init__(self, bank: 'Bank'):
        self.bank = bank

    # Run ATM machine
    def run(self, option: int):
        selected = int(option)
        if selected == 1:
            self.viewBalance()
        elif selected == 2:
            self.viewAccountDetails()
        elif selected == 3:
            self.withDrawMoney()
        elif selected == 4:
            self.ExitATM()
        else:
            print('Invalid option')

    # initialize the ATM machine
    def initialize(self, accountNumber: int):
        customer = self.bank.getAccount(accountNumber)
        self.customer = customer
        if isinstance(customer, Customer):
            print('******************************************')
            print(f'Hello {customer.fullname},')
            print('-----------------------------------------')
            print(f'Welcome to {self.bank.name} ATM machine')
            print('-----------------------------------------')
            print('Please you can select an option to proceed')
            print('------------------------------------------')
            print('Press 1. View Account Balance')
            print('Press 2. View Account Details')
            print('Press 3. Withdraw Money from')
            print('         Press c. current account')
            print('         Press s. savings account')
            print('Press 4. Exit ATM')
            print('*****************************************')
            return self
        else:
            return None

    # view account balance
    def viewBalance(self) -> str:
        print("Your remaining balance is {}".format(
            self.customer.wallet.fetchAllWallet()))

    # view account details
    def viewAccountDetails(self) -> dict:
        print("Your account details are: {}".format(self.customer.getDetails()))

    # exit ATM
    def ExitATM(self) -> str:
        self.isActive = False
        print("Goodbye {} thank your banking with us".format(
            self.customer.fullname))

     # withdraw money
    def withDrawMoney(self) -> str:
        if self.customer.logedInFailed < 3:

            wallet = str(
                input("Press c or s to Withdraw from: \n c. Current \n s. Savings \n: "))
            withdrawAccount = self.customer.wallet.fetchWallet(wallet)
            amount = int(input("Enter amount to withdraw: "))
            pin = int(input("Enter your account pin to withdraw: "))
            receipt = str(input("Do you want a printed receipt: yes/no :"))

            if pin == self.customer.pin:
                if amount > withdrawAccount:
                    print("You do not have enough money")
                    return
                else:
                    self.customer.wallet.debit(wallet, amount)
                    print("You have withdrawn {}".format(amount))
                    print(self.customer.wallet.fetchAllWallet())
                    if receipt == 'yes':
                        self.printReceipt(
                            amount, self.customer.wallet.current, self.customer.wallet.savings)
                    return
            else:
                self.customer.logedInFailed += 1
                print("Invalid transcation pin is incorrect")
                return
        print("You have reached the maximum number of failed attempts.Please contact your bank")

    @staticmethod
    def printReceipt(amount, current, savings):
        f = open("receipt.txt", "w")
        f.write("You have withdrawn {} \n".format(amount))
        f.write("Your current account balance is {} \n".format(current))
        f.write("Your savings account balance is {} \n".format(savings))
        f.close()

    @staticmethod
    def initializationFailed():
        print('ATM failed to initialize due to invalid card number')
