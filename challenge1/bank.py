from customer import Customer
from wallet import Wallet


class Bank:

    accountsCreated: int = 0

    def __init__(self, name: str, accounts: list = []):
        self.accounts = accounts
        self.name = name

    def addAccounts(self, *accounts: 'Customer'):
        for account in accounts:
            account.addWallet(Wallet())
            account.setPin()
            self.accounts.append(account)
            self.accountsCreated += 1

    def getAllAccounts(self):
        accounts: dict = {}
        for index, account in enumerate(self.accounts):
            accounts.update(
                {'ECO{}-{}'.format(index, account.accountNumber): account.getDetails()}
            )
        return accounts

    def getAccount(self, accountNumber: int):
        for account in self.accounts:
            if account.accountNumber == int(accountNumber):
                return account
        return 'Customer with account number {} does not exist'.format(accountNumber)

    @property
    def totalAccounts(self):
        return self.accountsCreated

    @staticmethod
    def customerNotFound(accountNumber: int):
        print('Customer with account number {} does not exist'.format(accountNumber))
