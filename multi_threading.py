#Multi_threading means running Multiple threads within the same program
#Threads share same memory space
#light weight and faster 
#easy to handling multiple user reqests(API calls), access Reading /writing files
#in python Multi-threading is a Global Interpter lock(GIL)
    #Only one thread executes pytho bytecode at a time

import threading
def task():
    print("task running")

t1=threading.Thread(target=task)
t2=threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()
