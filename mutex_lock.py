import threading
import time
from threading import *

shared_variable = 1

object = Lock()

def fun1():
    global shared_variable
    object.acquire()  
    x = shared_variable
    print("Thread1 reads the value as", x)
    x += 1  
    time.sleep(3)
    print("Value of shared variable updatedby Thread1 is:",x)
    object.release()

def fun2():
    global shared_variable
    object.acquire()  
    y = shared_variable
    print("Thread2 reads the value as", y)
    y-=1  
    time.sleep(3)
    print("Value of shared variable updatedby Thread2 is:",y)
    object.release()


thread1 = threading.Thread(target=fun1)
thread2 = threading.Thread(target=fun2)# start threads
thread1.start()
thread2.start()# wait for threads to finish
thread1.join()
thread2.join()# prints the last updated value of shared variable
print("Final value of shared is", shared_variable)