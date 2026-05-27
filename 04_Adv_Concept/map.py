
# WA1-1
num=[1,2,3,4,5,]

def square(x):
  return x*x

new =list(map(square,num)) #typecasting
print(new) 

# WAY-2

num1=[1,2,3,4,5,]
num2=[6,7,8,9,10]
multiply=map(lambda x,y : x*y,num1,num2)
print(list(multiply))