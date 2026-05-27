class Employee:
  def __init__(self,salary):
    self._salary=salary

  @property
  def get_salary(self):
   return self._salary
  
  @get_salary.setter
  def get_salary(self,sal):
    if(sal<0):
      print("sal never be negative!")
    else:
     self._salary=sal
  
e_1=Employee(50000)
print("Initial salary = ",e_1.get_salary)  
e_1.get_salary=-60000
print("Final salary = ",e_1.get_salary)# value of salary not change that's why 50000 again print