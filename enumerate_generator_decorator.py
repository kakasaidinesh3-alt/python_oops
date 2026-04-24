# Enumerate - enumerate is used to loop over an iterable and get the index and values at same time

#syntax - enumerate(iterable,start=0)
"""
l = ['jas','akjsj','uahd']
for i ,v in enumerate(l,start =0):
    #print(i,v)
    if i%2 ==0:
        print(v)


# next() is used in enumerate to get next element of index and element pair

l = ['x','y','z']
e = enumerate(l)
print(e)
print(next(e))

"""
#A generator in Python is a special type of function that produces values one at a time, instead of returning all values at once like a normal function.
#It uses the keyword yield instead of return.

"""
def gen(l):
    for i in l:
        yield i
        return 10
    

l =[1,2,3,4]

for i in gen(l):
    print(i)
"""
"""
#reverse the string 

def rev(s):
    l = len(s)-1
    for i in range(l,-1,-1):
        yield s[i]

s ="dinesh sai"
l =[]
for i in rev(s):
    l.append(i)

s = "".join(l)
print(s)
"""
"""
#reading the file

def files(file):
    with open(file,'r') as f:
        for line in f:
        #content = f.read()
            yield line

file = r'D:\python_class_part2\python_oops\data3.txt'

for i in files(file):
    print(i.strip())
"""
"""
#2. Processing Large Data (Streaming)

def large(n):
    for i in range(0,n):
        if i %2 ==0:
            yield i

l =[]
for i in large(1000):
    l.append(i)
print(l)


import requests

def fetch_users():
    page = 1
    
    while True:
        url = f"https://api.example.com/users?page={page}"
        response = requests.get(url)
        data = response.json()
        
        users = data.get("users", [])
        
        if not users:
            break   # no more pages
        
        for user in users:
            yield user   # yield one user at a time
        
        page += 1

for user in fetch_users():
    print(user["name"])

"""
"""
#Return the top K most frequent elements in a list?
l =[1,1,1,2,2,2,2,3,3,4,4,4,4,4,4,3,3,3]
d = {i: 0 for i in l}
for i in l:
    if d[i] ==0:
        d[i] = 1
    else:
        d[i]=d[i] +1
print(d)
l = list(d.values())
for i in range(0,len(l)-1):
    for j in range(i):
        if l[j] > l[j+1]:
            temp =l[j]
            l[j] = l[j+1]
            l[j+1] =temp
k =4
l1=[]
for i in range(0,k):
    l1.append(l[len(l)-i-1])
i =0
for key ,values in d.items():
    if values in l1:
        print(key)
"""
"""
l=[1,2,[3,[4,5,6],7,8],9]

def func(l):
    for i in l:
        if isinstance(i,list):
            yield from func(i) # Take every value produced by func(i) and yield it one by one from this function
        else:
            yield i

l1=[]
for x in func(l):
    l1.append(x)
print(l1)
"""
"""
#csv streaming(without loading whole file)
import csv

def file_data(file):
    l1 =[]
    l2 =[]
    d = {}
    with open(file,'r') as f:
        header = next(f).strip().split(',')
        for line in f:
            values = line.strip().split(",")
            yield dict(zip(header,values))

file = r'D:\python_class_part2\python_oops\data1.csv'
for line in file_data(file):
    if line["name"] == "dinesh":
        print(line)
"""
"""
# decorator is a function takes anotherfunction as input and return the new function 
import time
def my_dec(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("start:",start)
        print("end:",end)
        print("start-end:",end-start)
        print("even number in given list")
    return wrapper

@my_dec
def even():
    for i in range(10000):
        if i %2 ==0:
            print(i) 

even()
"""
"""
#added two element using decorator
import time
def my_dec(func):
    def wrapper(a,b):
        start = time.time()
        func(a,b)
        end = time.time()
        print("start-end:",start-end)
    return wrapper

@my_dec
def added(a,b):
    print(a+b)

added(2,3)
"""
"""
#even or odd
def my_dec(func):
    def wrapper(lst):
        func(lst)
    return wrapper

@my_dec
def even(l):
    for i in l:
        if i % 2 ==0:
            print("even:",i)
        else:
            print("odd:",i)

l = [1,2,3,4,5,6,7,8,9]
even(l)
"""
import logging
logging.basicConfig(filename="app.log",level=logging.INFO)

def my_dec(func):
    def wrapper(us,passw):
        #print("trying to logging")
        logging.info("tring to login")
        result =func(us,passw)
        if result:
            #print("successfully logged")
            logging.info("successfully logged")
        else:
            #print("logging failed")
            logging.error("logging failed")
    return wrapper

@my_dec
def auth(user,password):
    lst_user = ['dinesh','sai','kaka','pavan','zaheer']
    lst_password =['Dinesh@9700','Dinesh@7981','Sai$345','kaka*767','zahher*786']
    if user in lst_user and password in lst_password:
        #print("welcome to dashboard")
        logging.info("welcome to dashboard")
        return True
    else:
        #print("user and password wrong")
        logging.error("user and password wrong")
        return False

user ='dinesh'
password = 'Dinesh@970'
auth(user,password)