#what is file handling:
# file handling is used to handle the file for  create(),read(),write(),append(),close() purpose
"""
we have few modes to handle:
r -read() - Read-only. Raises I/O error if file doesn't exist.
r+ -read() - read and write Raises I/O error if file doesn't exist.
w- write() - write - only .overwrites files if it exists(),else create a new one.
w+ -write() - read ,write. Overwrites files or create new one.
a-append() - Append-only. Adds data to end. Creates file if it doesn't exist
a+ - append()- Read and append. Pointer at end. Creates file if it doesn't exist.
c-close()
x-create new file
wb-write binary- Write in binary. Overwrites or creates new.
wb + Read and write in binary. Overwrites or creates new.
rb-read binary - Read in binary mode. File must exist
rb + - Read and write in binary mode. File must exist.
ab - Append in binary. Creates file if not exist
ab+ - Read and append in binary. Creates file if it does not exist

"""
"""
#open() 

#here i using r - read only the data in file and if file is does not exists raise I/O Error
f = open("data.txt",'r')
print(f.read())
print(f.write("hii"))
#here i using r+ - read and write the data in file and if file is does not exists raise I/O Error
f = open("data.txt",'r+')
print(f.read())
print(f.write("hii\n"))
"""
"""
# w - write only create the file if does not exists- overwrite the existing data
f = open("data1.txt",'w')
print(f.write("hii im dinesh kaka\n"))
# w+ - write and read the data create the file if doesn't exists-overwrite the existing data
f = open("data2.txt",'w+')
print(f.write("hello dinesh im pythons\n"))
f.seek(0)
print(f.read())
"""
"""
# a - append is used to write the data in file ,without deleting the existing data , creating file is not avalible.
f = open("data2.txt",'a')
print(f.write("hjlik"))
"""
"""
# a + = append is used to read , write the data in a file without deleting the existing data, creating file is not avalible
f = open("data2.txt",'a+')
#f.seek(0)
#print(f.read())
#print(f.write("\nim learning python"))
#f.seek(0)
#print(f.readline()) # readline will print starting line of data in a file.
#print(f.readlines()) # readlines will print whole data in list format.
list1 =['sdmkds','jasjnd','njasj']
f.writelines(list1)
f.seek(0)
print(f.read())
"""
# with function in file handling , by with its automatically close the file, without corruption and memory leakages
"""
#custom expection:
import os

class FileNotFound(Exception):
    pass

file = r'D:\python_class_part2\python_oops\data2.txt'
try:
    if not os.path.exists(file):
        raise FileNotFound("file is not avalible")

    with open(file,'r') as f:
        c =f.readlines()
        print(c)
        for i in c:
            if 'dinesh' in i:
                print(i)

    
except Exception as e:
    print(e)

"""
"""
import os

list1 = ['jnjanjs','piyrtyuio','pokjnb','qwsdefgbn']
class FileNotFound(Exception):
    pass

file = r'D:\python_class_part2\python_oops\data3.txt'
try:
    with open(file,'w') as f:
        f.writelines(list1)

except Exception as e:
    print(e)

"""

# to handle csv files we have lib "import csv" and to handle excel file Import openpyxl or pandas
#to handle the csv files
#csv is comma seperator values
# to read the csv file
import csv
"""
with open("data.csv",'r') as fp:
    reader = csv.reader(fp)
    for  r in reader:
        print(r)

"""
"""
with open("data1.csv",'w') as f:
    w = csv.writer(f)
    w.writerow(['jskdkf','oiutt','ishhdsbd'])
"""
"""
l =[
    ['hsd','ksh','jsdjd'],
    ['nsj','jkkiu','iuytr'],
    ['poiuhj','azxds','gvbfd']
    ]

with open("data.csv",'a',newline='') as fp:
    w = csv.writer(fp)
    w.writerows(l)
"""

import os
import csv

class FileNotFound(Exception):
    pass

file = r'D:\python_class_part2\python_oops\data2.csv'
try:
    if not os.path.exists(file):
        raise FileNotFound("file is not avalible")

    with open(file,'r') as fp:
        r = csv.reader(fp)
        for i in r:
            print(i)

except Exception as e:
    print(e)




