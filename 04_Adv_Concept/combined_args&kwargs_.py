def combined(*args,**kwargs):
  
  print(args) # always printed tuple
  print(kwargs) #always printed dictionary pair

#jack=34,jill=32,marie=56 these are dictionary pair
combined(1,2,3,4,5,jack=34,jill=32,marie=56)
