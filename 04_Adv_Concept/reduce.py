from functools import reduce
num=[1,2,3,4,5]

# [3,3,4,5]
# [6,4,5]
# [10,5]
# [15]

def sum(a,b):
  return a+b

c=reduce(sum,num)
print(c)