class Employee :
  company = "HP"
  def get_salary(self) :# function called method in class
# self is important here because self is a way to reference the object of the class which is being created
    return 5000
  @staticmethod #decorator (changing the behavior of the normal function)
  #  use when no self parameter is required in method
  def  say_hello() :
    print("hello")

e_1=Employee() # Here OBJECT is class of Employee created 
print(e_1.get_salary()) #Employee get salary

del e_1
print(e_1)#Error show due to no e_1 object 
    