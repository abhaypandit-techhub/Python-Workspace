# while True:
#   try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(f"the sum is {a+b}")

#   except:
#     print("Some error occurred!")  

# while True:
#   try:
#     a=int(input("Enter a number: "))
#     b=int(input("Enter a number: "))
#     print(f"the sum is {a+b}")

#   except Exception as e:
#     print("Some error occurred!",e)  
    # print("Some error occurred!",e.add_note())  # gives more information about error

# 👉 Exception = error object
# ValueError ek built-in Exception class hai

# Types of error
while True:
  try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(f"the diviide is {a/b}")

  except ValueError:
    print("Please don't perform bad typecasts")  

  except ZeroDivisionError:
    print("cannot be don't divide by 0")   

  except Exception as e:
    print("Unknown error occurred!",e)  




          
  
