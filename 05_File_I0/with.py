# file=open("story.txt","r")
# content=file.read()
# print(content)
# file.close()

# BETTER APPROACH DOING SAME THINGS

with open("story.txt","r") as f: # also called context manager 
  content=f.read()
  print(content)
# NO need to write f.close() because file is already closed by default when using with syntax
