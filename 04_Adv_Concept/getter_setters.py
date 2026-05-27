class Employee :
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    
  #getter
  @property  
  def second_name(self):
    s=self.name.split(" ")
    print(s)
    return s[0]  
  
  #setter
  @second_name.setter
  def second_name(self,second_name):
    s=self.name.split(" ")
    new_name=f"{s[0]},{second_name}"
    self.name=new_name
  
e=Employee("Abhay Pandit",566)
# print(e.second_name())#without  using property decorator
print(e.second_name)#  # getter call
#using property decorator accessing name this way
# e.second_name("Prajapati")#without decorator
e.second_name="Prajapati"#without decorator,  setter call
print(e.name)
# e.location="india" 
# print(e.location)
