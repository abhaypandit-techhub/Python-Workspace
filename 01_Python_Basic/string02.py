n="abhay pandit"
b="\nabhay kumar "

print(n.title())
print(n.capitalize())
print(b.rstrip())
print(b.lstrip())
print(n.find("p"))
print(n.replace("abhay","kunal"))

fruits="apple,mango,banana"
print(fruits.split())  
print(",".join(['apple','mango','banana']))

# intro="My name is {} kumar. my father's name is {} kumar"
# a="Abhay"
# b=60000
# c="Deepak"

# substitute=intro.format(a,c)
# print(substitute)

a="Abhay"
b=60000
c="Deepak"

print(f"My name is {a} kumar. my father's name is {c} kumar")