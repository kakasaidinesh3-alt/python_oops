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
# w - write only create the file if does not exists- overwrite the existing data
f = open("data1.txt",'w')
print(f.write("hii im dinesh kaka\n"))
# w+ - write and read the data create the file if doesn't exists-overwrite the existing data
f = open("data2.txt",'w+')
print(f.write("hello dinesh im pythons\n"))
f.seek(0)
print(f.read())
