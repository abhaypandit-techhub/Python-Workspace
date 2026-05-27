# MULTI LAYER INHERITANCE

class animal : # Parent class (super class)
  location="Africa"

  def __init__(self,name) :
   self.name=name
  def speak_1(self):
    print("Generic animal sound")
  @staticmethod  
  def hello():
    print("how are you?")

  

  @staticmethod
  def sound():
    print("Roar")  


class dog(animal):# dog class inheritance from animal class
  def speak(self) :
    super().speak_1()#We are using speak function of parent class
    super().hello()
    print("Woof!")

  
class cat(dog):
  @staticmethod
  def sound():
    print(("meow meow")) 

b=cat("cristo")
# print(b.) 
b.speak()
print(b.location) # print because we inherit property of animal class in dig class 
b.sound()
print(b.name)