#what is data encapsulation?
#it is process to used make data and method in single unit or togther and controlling access of the data by using public, protected,private
#why encapsulation is need?
# for security purpose, easy to handle data,protect data from unautorized access
"""
class SBI_bank():
    def __init__(self,account_num,balance,password):
        self.account_num =account_num
        self._balance =balance
        self.__password = password

    def checking_pwd(self):
        return self.__password == self.user_password
    
class ATM(SBI_bank):
    def withdraw(self,amount_withdraw,user_password):
        self.amount_withdraw = amount_withdraw
        self.user_password = user_password
        if self.checking_pwd():
            if self.amount_withdraw <= self._balance:
                balance_amount = self._balance - self.amount_withdraw 
                print(balance_amount)
        
A = ATM(3453,9000,1234)
A.withdraw(1000,1234)
"""
#what is data abstraction?
# the method hides the implementation details and expose only essential features using abstract method and ABC 
from abc import ABC,abstractmethod

class bank(ABC):
    @abstractmethod
    def desposit(self):
        pass

    @abstractmethod
    def with_drawn(self):
        pass

    @abstractmethod
    def show_balance(self):
        pass

class ATM(bank):
    def __init__(self,balance):
        self.balance = balance

    def desposit(self,amount):
        self.balance += amount

    def with_drawn(self,withdraw_amount):
        if withdraw_amount <=self.balance :
            self.balance -=withdraw_amount
        else:
            print("insufficent_balance")
    
    def show_balance(self):
        print(f"{self.balance}")

a = ATM(9000)
a.show_balance()
a.with_drawn(10000)
a.show_balance()
a.desposit(2000)
a.show_balance()
