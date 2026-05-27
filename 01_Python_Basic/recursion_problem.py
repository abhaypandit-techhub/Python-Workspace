
#FIBONACCI NUMBER PRINT
# def factorial(n) :
#   if(n==1) :
#     return 0
#   elif(n==2) :
#     return 1
#   else :
#     return factorial (n-2)+factorial(n-1)
# n=int(input("Enter a number  : "))
# for i in range(1,n+1) :
#   print(factorial(i))

#FACTORIAL
# def factorial(n) :
#   if(n==1) :
#     return 1
#   else :
#     return factorial(n-1)*n
  
# n=int(input("Enter a number  : "))
# print(factorial(n))

def fibonacci(n) :
   if(n==1 or n==0) :
     return n
   return fibonacci (n-2)+fibonacci(n-1)
n=int(input("Enter a number"))
for i in range (0,n) :
  print(fibonacci(i))