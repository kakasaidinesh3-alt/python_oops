#polymorphism means same operation ,different behaviours
# it allows function and methods with same name but works differently based on object types and arguments used .
# types of polymorphism
#1. compile time polymorphism - method over loading
#2. run time polymorphism - operator overloading, method over riding, duck typing

#1) compile time polymorphism - method overloading 
# having multiple function or method with same name but works with different parameter(type or order)
"""
class A:
    def func1(self,a,b):
        print(a+b)
    def func1(self,a,b,c):
        print(a+b+c)

f = A()
f.func1(10,20)
f.func1(10,20,30)
#See here we used same method names but different parameter ,internally complier will take second func1 , first func1 wont take, seconf func1 overrides the first func1 due to that complier raise error "TypeError: A.func1() missing 1 required positional argument: 'c'"
# to avoid these we can use *args or default arguments
class A:
    
    def func1(self,*args):
        sum =0
        for i in args:
            sum = sum + i
        print("sum:",sum)
f = A()
f.func1(10,20)
f.func1(10,20,30)
"""
"""
#2. Runtime polymorphism:
# Method Overriding -: dervied class redefines the methods of base class with same name and parameter 
class SBI_bank:
    def __init__(self,account_no,amount_acc):
        self.account_no = account_no
        self.amount_acc = amount_acc
    
    def balance(self):
        
        print(f"{self.account_no} balance:{self.amount_acc}")

class ATM(SBI_bank):
    def __init__(self,account_no,amount_acc,with_drawn_amount):
        super().__init__(account_no,amount_acc)
        self.with_drawn_amount = with_drawn_amount
    def balance(self):
        print("before withdraw")
        super().balance()
        if self.with_drawn_amount <= self.amount_acc:
            self.amount_acc = self.amount_acc - self.with_drawn_amount
        print("ATM Transaction Completed")
        return super().balance()
    
    

A = ATM(5675,9000,1000)
A.balance()
"""

# Operator overloading : Operator  to behave differently for user-defined objects using special methods like __add__(),__sub__()..


class points:
    def __init__(self,x,y):
        self.x = x
        self.y =y
    
    def __add__(self,other):
        return self.x + other.x , self.y + other.y
    
    def __sub__(self, other):
        return self.x - other.x ,self.y - other.y
    
    
p1 =points(4,5)
p2 = points(7,8)
p3 = p1 + p2
print(p3)
p4 = p1-p2
print(p4)