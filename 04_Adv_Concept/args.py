def sum(*args):

#collect all the argument passed to function , args will be tuple 
# we can pass multiple value as argumnet using this concept

  print(args) # (342,2,7)
  total=0
  for item in args:
   total+=item
  return total

print(sum(342,2,7,49)) # 400