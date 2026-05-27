def average(a,b,c) :#def is kewword for writing a function
  d=(a+b+c)/2
  #print(d)

average(2,4,6)#passing of function
average(2,4,10)#passing of function

def add(a,b,plus=0) :
  x=a+b+plus
  return x
c=add(3,5,2) #due to this value of plus is 2
c=add(a=3,b=5) #due to this value of plus is remain 0 output will be 8
c=add(a=3,b=5,plus=2) #due to this value of plus is 2 output will be 10

print(c)

# LAMEDA FUNCTION

square=lambda x:x*x
sum=lambda y:y+5
print(square(9))
print(sum(8))
