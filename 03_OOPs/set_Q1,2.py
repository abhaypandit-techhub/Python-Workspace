#Question-1
# class car :
#   def drive(self):
#     return print("car is moving")
# c1=car()
# c1.drive()

#Question-2
class person :
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def bio(self):
    return  print(f"The person is {self.name} and its age is {self.age} year.")  
p_1=person("Abhay pandit",18)  
p_1.bio()
print(p_1.name,p_1.age)
  