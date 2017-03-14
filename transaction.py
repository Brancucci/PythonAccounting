class Transaction:
    """ A class used for transaction purposes

        Instance variables:
        amount -- the value amount of the transaction
        date -- the date the transaction took place
        currency -- the currency used in the transaction
        usd_conversion_rate -- the conversion rate multiplier to use to convert to USD
        description -- description of the transaction

        """

    # class initializer :: note: __ before a class instance variable makes it private
    def __init__(self, amount, date, currency="USD", conversion=1, description=None):
        self.__amount = amount  # private read only
        self.__date = date  # private read only
        self.__currency = currency  # private read only
        self.__usd_conversion_rate = conversion  # private read only
        self.__description = description  # private read only

    @property
    def amount(self):
        """ Method for getting the amount """
        return self.__amount

    @property
    def date(self):
        """ Method for getting the date """
        return self.__date

    @property
    def currency(self):
        """ Method for getting currency """
        return self.__currency

    @property
    def usd_conversion_rate(self):
        """ Method for getting the usd conversion rate """
        return self.__usd_conversion_rate

    @property
    def description(self):
        """ Method for getting the description """
        return self.__description

    @property
    def usd(self):
        """" Method for calculating amount in US dollars """
        return self.__amount * self.__usd_conversion_rate




