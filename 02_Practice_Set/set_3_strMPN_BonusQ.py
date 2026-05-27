text="coding in python is fun"
print(text.replace("fun","awesome"))
print(text.upper())
print(text.index("python"))
#Bonus Question

# Q1
vowels = ['a','e','i','o','u']
sum = 0
for char in text.lower() :
  if char in vowels :
    sum=sum + 1 

print(f"The of number vowels in text string is {sum} ")

#Q2

n=input("Enter a string :")
if n[::-1] == n:
  print("String is palindrome")
else :
  print("Strng is not palindrome")