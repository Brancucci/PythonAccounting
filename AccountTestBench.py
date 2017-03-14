from account import Account
from transaction import Transaction
import os
import tempfile

"""
    sample code
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """


# test code for transaction class
t = Transaction(100, "2008-12-09")
print(t.amount, t.currency, t.usd_conversion_rate, t.usd)
t = Transaction(250, "2009-03-12", "EUR", 1.53)
print(t.amount, t.currency, t.usd_conversion_rate, t.usd)

print('\n"Testing Acount" \n')

# test code for account class
account = Account(123456789, "Anthony")
print("The account number is: {} and the account name is: {}".format(account.account_num, account.account_name))
print("#: {} name: {} balance: {} all_usd: {} length: {} ".format(account.account_num, account.account_name, account.balance, account.all_usd, len(account)))
account.apply(Transaction(100, "2008-11-14"))
account.apply(Transaction(150, "2008-12-09"))
account.apply(Transaction(-95, "2009-01-22"))
print("#: {} name: {} balance: {} all_usd: {} length: {} ".format(account.account_num, account.account_name, account.balance, account.all_usd, len(account)))
account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
print("#: {} name: {} balance: {} all_usd: {} length: {} ".format(account.account_num, account.account_name, account.balance, account.all_usd, len(account)))
account.save()
newaccount = Account(123456789, "Anthony")
print("new account info: {}  {}  {}".format(newaccount.balance, newaccount.all_usd, len(newaccount)))
newaccount.load()
print("new account info: {} {} {}".format(newaccount.balance, newaccount.all_usd, len(newaccount)))


