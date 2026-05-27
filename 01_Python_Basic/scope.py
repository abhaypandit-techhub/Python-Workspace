def sum(a,b) :
  ''' The sum of the two number'''
  c=a+b
  global z # global keyword used to modify global z(only define in function)
  z=10 # this now a global variable not a local variable
  # z=50 # local variable
  return c

print(sum.__doc__)
z=100 # global variable
print(sum(2,5))
print(z)

