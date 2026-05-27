
try:

  f=open("bio.txt","r")

  for  line in f:
   print(line)
  f.close()

except Exception as e:
  print(e)  

# except FileNotFoundError as e:
#   print(e)  
