a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if b==0:
  raise ValueError("cann't divide by 0")
print(f" the division is {a/b}")