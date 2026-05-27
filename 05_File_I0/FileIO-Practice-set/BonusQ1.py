with open("tasks.txt","r") as f:
  content=f.read()
  print(content)

# content text converted into lower case character 
with open("outputUPPER.txt","w") as f:
  f.write(content.lower())  