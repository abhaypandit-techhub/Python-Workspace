
#Q1
import math 
import requests
fetch=requests.get("https://api.github.com")
print(fetch.text)
print(math.sqrt(144))
print(math.sin(math.radians(90)))

#Q2

def increment() :
  counter=0
  counter=counter+1
  return counter  
print(increment())
print(increment())
print(increment())

#Q3
def multiply(a,b):
  '''Here we multiiply two number a,b
    using function multiply'''
  return a*a
# print(multiply.__doc__)
print(multiply(2,5))
help(multiply)

#Q bonus challenge

import mymodule 
a=int(input("Enter a number: "))
if mymodule.even(a) :
  print("Even number : ")
else :
  print(" Not even number :")





