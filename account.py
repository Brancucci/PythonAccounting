import pickle


class Account:
    """ A class used to store accounts of users

    Instance variables:
    account_num -- the account number
    account_name -- the name on the account
    transactions -- a list of transactions

    """

    # initializing an account
    def __init__(self, acc_num, acc_name):
        """ Initialize an account """
        self.__account_num = acc_num  # read only
        self.__account_name = acc_name  # read / write property need assertion to make sure name is > 4 char long
        self.transactions = []

    # a function to return the number of transactions
    def __len__(self):
        """ Method for returning the number of transactions in given account """
        return len(self.transactions)

    @property
    def account_num(self):
        """ Method for getting account number """
        return str(self.__account_num)

    @property
    def account_name(self):
        """ Method for getting account name """
        return self.__account_name

    @account_name.setter
    def account_name(self, acc_name):
        """ Method for getting the account name """
        if len(acc_name) < 4:
            raise ValueError("Account name must be longer than 4 characters")
        self.__account_name = acc_name

    @property
    def balance(self):
        """ Returns the account balance """
        balance = 0.0
        for item in self.transactions:
            balance += item.usd
        return balance

    @property
    def all_usd(self):
        """Method that returns true if all the transactions were in USD """
        allUs = True
        for item in self.transactions:
            if item.currency != "USD":
                allUs = False
        return allUs

    def apply(self, trans):
        """ Applies (adds) a transaction to the transaction history """
        t = trans
        self.transactions.append(t)

    def save(self):
        """ Saves the account number, name, and transaction history """
        information = [self.account_num, self.account_name, self.transactions]
        file = '' + self.account_num + '.acc'
        pickle.dump(information, open(file, "wb"))

    def load(self):
        """ Loads the account number, name, and transaction history """
        file = '' + self.account_num + '.acc'
        information = pickle.load(open(file, "rb"))
        self.account_name = information[1]
        self.transactions = information[2]






