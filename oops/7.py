# M1. Extend the BankAccount class: add a class attribute total_accounts that increases by 1 every time a new
# account is created. Print it after making 3 accounts.
# Hint: increment the class attribute inside __init__.

class BankAccount:
      total_accounts = 0

      def __init__(self, account_number):

            self.account_number = account_number

            BankAccount.total_accounts +=1

account1 = BankAccount(101)
account2 = BankAccount(102)
account3 = BankAccount(103)

print("Total accounts :", BankAccount.total_accounts)
