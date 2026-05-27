class Employee :
  company="HP"#This is the class attribute
  def __init__(self,salary,name,bond,company):#constructor , these takes some parameter
    # create an instance attribute of name salary and assign it with salary 
    self.salary=salary
    self.name=name
    self.bond=bond
    self.company=company
  def get_info(self):# here function is called method
    return f"The Employee name is {self.name}.salary is {self.salary}.The bond is {self.bond} year." 

e_1=Employee(45000,"Abhay",4,"ASUS")
print(e_1.company) #will always print instance attribute whenever present
print(Employee.company) #always printed class printed attribute
# e_2=Employee(55000,"kunal",5)
# print(e_1.get_info())
# print(e_2.get_info())

# OBJECT INTROSPECTION
print(dir(e_1)) 