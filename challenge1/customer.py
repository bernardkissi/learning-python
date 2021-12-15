from wallet import Wallet
import random


class Customer:
    def __init__(self,
                 fname: str,
                 lname: str,
                 address: str,
                 accountNumber: int,
                 email: str,
                 logedInFailed: int = 0,
                 ):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.email = email
        self.logedInFailed = logedInFailed
        self.accountNumber = accountNumber

    @property
    def fullname(self) -> str:
        return '{} {}'.format(self.fname, self.lname)

    def setPin(self):
        self.pin = random.randint(1000, 9999)

    def getDetails(self) -> dict:
        return {
            "firstname": self.fname,
            "lastname": self.lname,
            "age": 32,
            "address": self.address,
            "email": self.email,
            "pin": self.pin,
            "logedInFailed": self.logedInFailed,
            "accountNumber": self.accountNumber,
            "wallet": self.wallet.fetchAllWallet()
        }

    def addWallet(self, wallet: Wallet):
        self.wallet = wallet
