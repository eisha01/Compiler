import threading

# Create a semaphore with two resources
semaphore = threading.Semaphore(2)


def thread_function(thread_name):
 
  semaphore.acquire()
  print(f"{thread_name} acquired a resource")
  
  
  print(f"{thread_name} is working")
  
 
  print(f"{thread_name} released a resource")
  semaphore.release()


thread1 = threading.Thread(target=thread_function, args=("Thread 1",))
thread2 = threading.Thread(target=thread_function, args=("Thread 2",))
thread3 = threading.Thread(target=thread_function, args=("Thread 3",))

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for the threads to finish
thread1.join()
thread2.join()
thread3.join()

print("All threads have finished")