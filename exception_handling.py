#what is exception handling?
# Exception handling is a mechanism to handle the run-time error by using try,except,else and finally keywords will helps to prevent the program from crashing
#try: try keyword used for write code inside the block
# except : except is used to raise the Exception based the try block code or script
# else : else is used for when try is success then else will execute
# finally: whatever condition happen in try or except  ,defintely finally block will execute 
# raise : raise is used to throw an error by using bulit -in -exception(zeroDivisionerror,valueerror,typeerror) and custom exception(user-defined) 
"""
a =10
b =2
try:
    ans = a//b
    print(ans)
except ZeroDivisionError:
    print("num shouldnt dividual by zero")

try:
    ans = a//b
    print(ans)
except Exception as e:
    print(e)
else:
    print("successfull without exception\n")

finally:
    print("completed\n")
"""
"""
a =10
b =20
try:
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("string can be added\n")
    c = a + b
    print(c)
    
except TypeError as e:
    print(e)
"""
"""
a =""
b =2
print(type(a))
try:
    if isinstance(a,int):
        if b ==0:
            raise ZeroDivisionError("zero cant be divided")
        else:
            print(a//b)
    else:
        raise TypeError("a is not integer\n")
    
except (ZeroDivisionError,TypeError) as e:
    print(e)

"""
#custom Exception: custom exception is a user-defined to create the excetion class to handle the application specific error
#only with raise:
"""
class AgeInvalid(Exception):
    pass

age = 17

if age<18:
    raise AgeInvalid("age is less the 18\n")
print(age)
"""
"""
#write a code with custom exception by using try and except?
class AgeNotValid(Exception):
    pass

age = int(input("enter the num\n"))

try:
    if age <18:
        raise AgeNotValid("age is less than 18")
    print(age)
except Exception as e:
    print(e)
"""
#write a custom exception to handle the marks of 5 students
class MarksInvalid(Exception):
    pass

class Student:
    def __init__(self,marks):
        if marks<=0 or marks >100:
            raise MarksInvalid("marks should be between 0 to 100\n")
        self.marks = marks
    def printf(self):
        print("self.marks:",self.marks)

student_marks =[]
try:
    for i in range(0,3):
        marks =int(input("enter the num\n"))
        student_marks.append(Student(marks))

    for i in range(0,3):
        student_marks[i].printf()
        
except Exception as e:
            print(e)
