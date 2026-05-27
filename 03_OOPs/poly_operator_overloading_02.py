#ADDING TWO COMPLEX NUMBER
# class complex :
#   def __init__(self,real,img):
#     self.real=real
#     self.img=img

#   def show_Number(self):
#     print(self.real,"i +",self.img,"j")  

#   def add(self,num_2):
#     new_real=self.real + num_2.real
#     new_img=self.img + num_2.img
#     return complex( new_real,new_img)

# num_1=complex(2,5)
# num_2=complex(4,1)
# num_1.show_Number()    
# num_2.show_Number()

# num_3=num_1.add(num_2)  
# num_3.show_Number() 


#ADDING COMPLEX NUMBER BETTER WAY
#using dunder function
#OPERATOR OVERLOADING
class complex :
  def __init__(self,real,img):
    self.real=real
    self.img=img

  def show_Number(self):
    print(self.real,"i +",self.img,"j")  

  def __add__(self,num_2): # num2 object of class and .real attribute of that object(data member)
    new_real=self.real + num_2.real
    new_img=self.img + num_2.img
    return complex( new_real,new_img)

num_1=complex(2,5)
num_2=complex(4,1)

num_1.show_Number()    
num_2.show_Number()

num_3=num_1+num_2 # python convert internaly num_1.__add__(num_2)
num_3.show_Number()