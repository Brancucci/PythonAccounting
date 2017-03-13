
class Transaction:
    """ A class used for transaction purposes """

    # class initializer :: note: __ before a class instance variable makes it private
    def __init__(self, amount, date, currency="USD", conversion=1, description=None):
        self.__amount = amount  # private read only
        self.__date = date  # private read only
        self.__currency = currency  # private read only
        self.__usd_conversion_rate = conversion  # private read only
        self.__description = description  # private read only

    # TODO remove this print statement
    @property
    def amount(self):
        """ Method for getting the amount """
        print("Getting amount")
        return self.__amount

    # TODO remove this print statement
    @property
    def date(self):
        """ Method for getting the date """
        print("Getting date")
        return self.__date

    # TODO remove this print statement
    @property
    def currency(self):
        """ Method for getting currency """
        print("Getting currency")
        return self.__currency

    # TODO remove this print statement
    @property
    def usd_conversion_rate(self):
        """ Method for getting the usd conversion rate """
        print("Getting usf conversion rate")
        return self.__usd_conversion_rate

    # TODO remove this print statement
    @property
    def description(self):
        """ Method for getting the description """
        print("Getting the description")
        return self.__description

    # TODO remove this print statement
    @property
    def usd(self):
        """" Method for calculating amount in US dollars """
        print("Getting the amount in us dollars")
        return self.__amount * self.__usd_conversion_rate




