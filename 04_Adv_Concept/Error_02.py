# Types of error
while True:

  try:
    a=int(input("Enter a number: "))
    b=int(input("Enter a number: "))
    print(f"the diviide is {a/b}")

  except (ValueError,ZeroDivisionError) as e:
    print("Unknown error occurred!",e)    
