#Q1

# name="John"
# age=25
# intro="My name is {} and i am {} years old."
# print(intro.format(name,age))# using format method
# print(f"My name is {name} and i am {age} years old.")# f- string method

#Q2

text_1=" i love python programming "
# print(text.strip())
# print(text.title())

# method 1 for counting character

#Q3
i=0
count=0
char="o"
while i< len(text_1):
  if text_1[i]==char :
    count=count+1
  i=i+1

print(f"The number of times o character is reapeted in text is {count} ") 

# method 2 for counting character
print(text_1.count("o"))
   

#Q4

text_2="123abc"   
if text_2.isalnum() : 
  print("This string is alphanumeric")
else :
  print("This is not alphanumeric character ")  

