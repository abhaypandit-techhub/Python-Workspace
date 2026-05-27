#EMPLOYEE DETAILS

class Employee :
  # def __init__(self) : in non parametrized constructor we must to ptovide value of eg. self.name="abhay" 
  def __init__(self,ID,Name,Designation,salary) :
    self.ID=ID
    self.Name=Name
    self.Designation=Designation
    self.salary=salary

  def emp_1_information (self) :
    print((f"{self.ID}\t\t{self.Name}\t\t{self.Designation}\t\t\t{self.salary}") )

  # def emp_2_infromation (self):
  #   print((f"{self.ID}\t\t{self.Name}\t\t{self.Designation}\t{self.salary}") )

print("\t\t******Employee Details******")    
print("ID\t\tNAME\t\tDESIGNATION\t\tSALARY") 
e_1=Employee(245,"kunal","SDE",45000)
e_2=Employee(246,"Alok","SDE",40000)
e_3=Employee(247,"Abhay","SDE",44000)
e_4=Employee(248,"Ram","SDE",50000)
e_5=Employee(249,"Bittu","SDE",49000)

employees =[e_1,e_2,e_3,e_4,e_5]

for e in employees  :
  e.emp_1_information()


    