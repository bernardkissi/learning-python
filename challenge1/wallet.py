class Wallet:

    def __init__(self, current: int = 200, savings: int = 300):
        self.currentWallet = current
        self.savingsWallet = savings

    @property
    def current(self):
        return self.currentWallet

    @property
    def savings(self):
        return self.savingsWallet

    @current.setter
    def current(self, amount: int):
        self.currentWallet = amount

    @savings.setter
    def current(self, amount: int):
        self.savingsWallet = amount

    def credit(self, type: str, amount: int):
        if type == "c":
            self.currentWallet += amount
        elif type == "s":
            self.savingsWallet += amount
        else:
            print("Invalid type")

    def debit(self, type: str, amount: int):
        if type == "c":
            self.currentWallet -= amount
        elif type == "s":
            self.savingsWallet -= amount
        else:
            print("Invalid type")

    def fetchAllWallet(self):
        return {
            "Current account balance is ": self.currentWallet,
            "Savings account balance is": self.savingsWallet
        }

    def fetchWallet(self, type: str):
        if type == "c":
            return self.currentWallet
        elif type == "s":
            return self.savingsWallet
        else:
            print("Invalid type")
