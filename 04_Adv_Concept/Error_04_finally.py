def divide(a,b):
  try:
      c=a/b
      print(c)

  except Exception as e: 
     print(e)   

  finally:
     print("This is always executed")
# This line is always executed if try block completly execute or not
# print("This is always executed") #not applicable here finally can be used it

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
divide(a,b)
