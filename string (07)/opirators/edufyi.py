class bankoperation():
      def __init__(self,balance):
            self.balance = balance
            # print("balance =",self.balance)


      def deposit(self,money):
            print("Money Deposited", money)
            self.balance = self.balance + money
            print("balance =",self.balance)

      def withdrawal(self,money):
            if self.balance >= money :
                print("Withdrawal Money :",money)
            
                self.balance = self.balance -money  

                print("balance =",self.balance)

# bank_balance = bankoperation(500)

# bank_balance.deposit(3000)

# bank_balance.withdrawal(226)

class BankHistory(bankoperation):
      
      def __init__(self,balance):
            super().__init__(balance)
        
            print("Transection History =",self.balance)

user = BankHistory(500)

bank_balance = bankoperation(500)

bank_balance.deposit(3000)

bank_balance.withdrawal(226)  





                  

