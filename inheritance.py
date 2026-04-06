#what is inheritance in python?
#inheritance is used to derived class inherit the properties and methods, attributes in base class.

"""what are the types of inheritance in python?
1.single inheritance
2.mulitple inheritance
3.multileave inheritance
4.hierarchical inheritance
5.hybrid inheritance"""

#1.single inheritance:
#dreived class inherit the properties and methonds of base class in called single inheritance.
"""
class father:
    def __init__(self,father_name,father_age,father_property):
        self.father_name =father_name
        self.father_age = father_age
        self.father_property = father_property
    def printf(self):
        print(self.father_name,self.father_age,self.father_property)

class child(father):
    def __init__(self, name, age, property,father_name,father_age,father_property):
        father.__init__(self,father_name,father_age,father_property)
        self.child_name = name
        self.child_age =  age
        self.child_property = property

    def print(self):
        print(self.child_name,self.child_age,self.child_property)

    def add_property(self):
        self.total = self.father_property + self.child_property
        print("self.total:",self.total)
    

c = child("dinesh",29,5000,"yugandhar",54,10000)
c.print()
c.printf()
c.add_property()
"""
"""
#multiple inheritance
#derived class inherit the properties and attrtibutes and methods of more than one base class.
class grand_father:
    def __init__(self,grand_father_name,grand_father_age,grand_father_property):
        self.grand_father_name = grand_father_name
        self.grand_father_age = grand_father_age
        self.grand_father_property = grand_father_property
    def grand_father_print(self):
        print(self.grand_father_name,self.grand_father_age,self.grand_father_property)

class father:
    def __init__(self,father_name,father_age,father_property):
        self.father_name =father_name
        self.father_age = father_age
        self.father_property = father_property
    
    def father_print(self):
        print(self.father_name,self.father_age,self.father_property)

class son(grand_father,father):
    def __init__(self, grand_father_name, grand_father_age, grand_father_property,father_name,father_age,father_property,son_name,son_age,son_property):
        grand_father.__init__(self,grand_father_name,grand_father_age,grand_father_property)
        father.__init__(self,father_name,father_age,father_property)
        self.son_name =son_name
        self.son_age = son_age
        self.son_property = son_property

    def son_print(self):
        print(self.son_name,self.son_age,self.son_property)
        
    def inherit_property(self):
        self.son_property = self.father_property+ self.grand_father_property + self.son_property
        print("self.son_property:",self.son_property)
    


s = son("brahim",75,80000,"yugandhar" ,54,50000,"dinesh",29,20000)
s.son_print()
s.father_print()
s.grand_father_print()
s.inherit_property()
"""
"""
# Multi_Level Inheritance
# derived class inherit the base class which inherit the another derived class.
class Grand_father:
    def __init__(self,grandfather_name,grandfather_age,grandfather_property):
        self.grandfather_name = grandfather_name
        self.grandfather_age = grandfather_age
        self.grandfather_property = grandfather_property

class father(Grand_father):
    def __init__(self, grandfather_name, grandfather_age, grandfather_property):
        Grand_father.__init__(self,grandfather_name, grandfather_age, grandfather_property)
        pass

class son(father):
    def __init__(self, grandfather_name, grandfather_age, grandfather_property):
        father.__init__(self,grandfather_name,grandfather_age,grandfather_property)
        self.son_property = self.grandfather_property

    def printf(self):
        print(self.grandfather_name,self.grandfather_age,self.grandfather_property,self.son_property)
    
s = son("bhrami",75,900000)
s.printf()
"""
#Hierachical inhertance 
# two or more than derived class inherits from base class.
class father:
    def __init__(self,name,age,father_property):
        self.name = name
        self.age = age
        self.father_property = father_property
    
    def property_divided(self):
        self.share = self.father_property/3
        print(f"{self.name} gets:{self.share}")

class son1(father):
    def __init__(self,name,age,father_property):
        father.__init__(self,name,age,father_property)
        pass

class son2(father):
    def __init__(self, name, age, father_property):
        father.__init__(self,name,age,father_property)
        pass

class son3(father):
    def __init__(self, name, age, father_property):
        father.__init__(self,name,age,father_property)
        pass


s1 = father("dinesh",29,9000000)
s2 = father("keerthi",27,9000000)
s3 = father("raghav",27,9000000)

s1.property_divided()
s2.property_divided()
s3.property_divided()
