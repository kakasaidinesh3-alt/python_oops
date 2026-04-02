"""
#simple class
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printf(self):
        print(self.name,self.age)

s = Student("dinesh",56)
s.printf()
"""

#mention 5 student in class
class student: #created the class
    def __init__(self,name): # intilazing the attribute in a class
        self.name = name

    def print(self):
        print(self.name)

student1=[] #object list

for i in range(5):
    name = input("enter the name:\n")
    student1.append(student(name)) #call object instance of class

for i in range(5):
    student1[i].print() #object call the print function