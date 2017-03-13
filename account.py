
class Account:
    """ A class used to store accounts of users """

    # initializing an account
    def __init__(self, acc_num, acc_name, trans=[]):
        """ Initialize an account """
        self.__account_num = acc_num  # read only
        self.__account_name = acc_name  # read / write property need assertion to make sure name is > 4 char long
        self.__transactions = trans

    # a function to return the number of transactions
    def __len__(self):
        """ Method for returning the number of transactions in given account """
        pass

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




