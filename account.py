import os
import tempfile


class Account:
    """ A class used to store accounts of users """



    # initializing an account
    def __init__(self, acc_num, acc_name):
        """ Initialize an account """
        self.__account_num = acc_num  # read only
        self.__account_name = acc_name  # read / write property need assertion to make sure name is > 4 char long
        self.__transactions = []

    # a function to return the number of transactions
    def __len__(self):
        """ Method for returning the number of transactions in given account """
        return len(self.__transactions)

    # TODO remove this print statement
    @property
    def account_num(self):
        """ Method for getting account number """
        print("using property: Getting account number value")
        return self.__account_num

    # TODO remove this print statement
    @property
    def account_name(self):
        """ Method for getting account name """
        print("using property: Getting account name")
        return self.__account_name

    # TODO remove this print statement
    @account_name.setter
    def account_name(self, acc_name):
        """ Method for getting the account name """
        print("using property: setting account name")
        if len(acc_name) < 4:
            raise ValueError("Account name must be longer than 4 characters")
        self.__account_name = acc_name


    @property
    def balance(self):
        """ Returns the account balance """
        pass

    #TODO remove the print statement
    @property
    def all_usd(self):
        """Method that returns true if all the transactions were in USD """
        pass

    def apply(self):
        """ Applies (adds) a transaction to the transaction history """
        pass

    def save(self):
        """ Saves the account number, name, and transaction history """
        pass

    def load(self):
        """ Loads the account number, name, and transaction history """
        pass



