class Employee :
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary

  def __str__(self):
    return f"The name is {self.name} and salary is {self.salary}."  
  
  def __repr__(self):
    return f"The name is {self.name} and salary is {self.salary}."  
  
  def __len__(self): # used for length of the string calculation
    return len(self.name)

e=Employee("Harry",45600)
print(e.name,e.salary)
print(str(e)) # python internaly doing str(e)=e.__str__()
print(repr(e)) # python internaly doing str(e)=e.__repr__(),mostly use developer
print(len(e)) # gives length of string
print(e)
