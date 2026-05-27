
from time import time
def timer(func):
  def wrapper(n):
    t1=time()# start time
    result=func(n)# original function call
    t2=time()# end time
    print(t2-t1) # time difference
    return result
  return wrapper  

@timer # reason for use sum1_1m = timer(sum1_1m)
def sum1_1m(n):
  sum=0
  for i in range(1,n+1):
    sum=sum+i
  return sum 
a=sum1_1m(1000000) 
print(a)

