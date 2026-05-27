import threading
import time
def worker(num):
  print(f"Thread {num}: starting") # starting a threads
  time.sleep(2) # wait for two second keep holding the program for two second, simulate some work
  print(f"Thread {num}:Finishing") # Finishing the threads

  threads=[]
  for i in range(3):
    thread=threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()

  for thread in threads:
      thread.join()# wait for all threads to finish
  print("All threads completed.")