#Q1
def greet() :
  print("Hello, Python learner!")
greet()

#Q2
# def square(num) :
#   return num*num
# a=int(input("Enter a number :")) 
# print(square(a))

#Q3
def full_name(first,last) :
  return f"{first} {last}"
print(full_name("Abhay","kumar"))

#Q4
# def calculate_area(length,width=10) :
#   return length*width
# print(calculate_area(5.0,7.9))
# print(calculate_area(5.0))

#Q5
add=lambda x,y:x+y
print(f"The addition of two number is {add(8,9)}")

#Q6
# square=lambda x :x*x
# list_1=[1,2,3,4,5]
# result=list(map(square,list_1))
# print(result)

#Q8 m-1
def sum_of_digit(n) :
  sum=0
  while n>0 :
    rem=n%10
    sum=sum+rem
    n=n//10
  return sum

print(sum_of_digit(34))

# m-2
def sum_of_digit(n) :
  if n == 0:
    return 0
  
  return n%10 + sum_of_digit(n//10)
print(sum_of_digit(56))

#Q9
def safe_divide(a,b):
  if(b==0) :
    return print("a is cannot divide by b")
  else :
    return a/b
  
a=int(input("Enter a value of a : "))
b=int(input("Enter a value of b : "))
print(safe_divide(a,b))

