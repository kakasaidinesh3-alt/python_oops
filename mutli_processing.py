from multiprocessing import Process

def task():
    print("process running")
    
if __name__ == "__main__":

    p1 = Process(target=task)
    p2 = Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
