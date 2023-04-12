import threading
import time
import os
import mutex_lock

x = 2
lock = threading.Lock()

def  multiply():
    global x, lock
    lock.acquire()
    print("after multiply the value is : ")
    x *= 2
    print(x)
    time.sleep(3)
    lock.release()

def  add():
    global x, lock
    lock.acquire()
    print("after multiply the value is : ", )
    x *= 3
    print(x)
    time.sleep(3)
    lock.release()


t1 = threading.Thread(target=multiply)
t2 = threading.Thread(target=add)

t1.start()
t2.start()

