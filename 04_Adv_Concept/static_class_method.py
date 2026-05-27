class Employee:
  company="HP"
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
#Instance method (default)
  def print_info(self):
    return print(f"The name is {self.name} and the salary is {self.salary}")
  
  #static method
  @staticmethod
  def sum(a,b):
    return a+b
  
  # We need this class for employee inside this method

  @classmethod
  def change_company(cls,new_company):
    cls.company=new_company

  @classmethod
  def print_company(cls):
    return cls.company

e1=Employee("Abhay",45000)    
e2=Employee("Kunal",50000)  

e1.print_info()
e2.print_info()
print(e1.sum(3,6))
# e1.change_company("DELL")#HP
Employee.change_company("HP")
print(Employee.print_company())
# e1.print_company()#HP

