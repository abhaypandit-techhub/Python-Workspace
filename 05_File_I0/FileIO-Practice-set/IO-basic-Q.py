# file=open("notes.txt",'r')
# content=file.read()
# print(content)
# file.close()

# BEST WAY
with open("notes.txt",'r') as file:
  content=file.read()
  print(content)

