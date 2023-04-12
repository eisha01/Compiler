import threading
import time
from threading import *

shared_variable = 1


def increment_value():   
    time.sleep(3)            
    print("the incremented value is: ",shared_variable+1)
    

def decrement_value():
     time.sleep(3)    
     print("the decremented value is: ",shared_variable-1)
    
    

t=threading.Thread(target=increment_value)
t2=threading.Thread(target=decrement_value)

t.start()
t.join()

t2.start()
t2.join()

