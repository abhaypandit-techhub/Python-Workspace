class calculator:
  def __init__ (self,x,y):
    self.x=x
    self.y=y

  def add(self):
    print("x+y =",self.x+self.y)

  def subtract(self):
    print("x-y =",self.x-self.y)  

  def multiplication(self):
    print("x*y =",(self.x)*(self.y))  

  def division(self):
    print("x/y =",(self.x)/(self.y))


print("\n(A)Press '1' for Addition\n(B)Press '2' for Subtraction\n(C)Press '3' for Multiplication\n(D)Press '4' for Division")
num=int(input("Press for requird operation : "))
x=int(input("Enter a value of x : "))
y=int(input("Enter a value of y : "))
operation=calculator(x,y)    


if(num==1) :
  operation.add()

elif(num==2) :
 operation.subtract()
  
elif(num==3):
 operation.multiplication()

elif(num==4):
 operation.division()