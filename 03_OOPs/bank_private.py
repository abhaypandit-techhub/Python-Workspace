class Account :
  # private attribute
  def __init__(self,balance,account,password):
    self.balance=balance
    self.account=account
    self.__password=password #this is private attribute/variable we cannot access outside the class
    # using double underscore(__) to create private attribute 

  def debit(self,amount):
    self.balance-=amount
    print(amount,"debited")
    print("Total balance = ",self.balance)

 
  def credit(self,amount):
    self.balance+=amount
    print(amount,"credited")
    print("Total balance = ",self.balance)

  def reset_passw(self):#we access through a method private attribute
    print(self.__password)  
  
aval=Account(5000,2355314458776,"abhay@3456") 
aval.debit(500)
aval.credit(10000)
# print(aval.__password) it show error not able to access
aval.reset_passw()
  