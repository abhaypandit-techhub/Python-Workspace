# class student :
# In that case average value does not change during attribute changes
 
#   def __init__(self,phy,chem,math):
#     self.phy=phy
#     self.chem=chem
#     self.math=math
#     self.average=str((self.phy+self.chem+self.math)/3)+"%"
# stud_1=student(94,90,99)
# stud_1.chem=92
# print(stud_1.average)    
# print(stud_1.chem)    
# print(stud_1.average)    


# UPDATE-1
#In that case average value change during attribute changes 
# class student :
#   def __init__(self,phy,chem,math):
#     self.phy=phy
#     self.chem=chem
#     self.math=math
#     self.average=str((self.phy+self.chem+self.math)/3)+"%"

  
#   def average_new(self):
#     self.average=str((self.phy+self.chem+self.math)/3)+"%"
  
# stud_1=student(94,90,99)
# stud_1.chem=92
# print(stud_1.average)    
# print(stud_1.chem)    
# stud_1.average_new()
# print(stud_1.average)  


# UPDATE_2 BETTER WAY
class student :
  def __init__(self,phy,chem,math):
    self.phy=phy
    self.chem=chem
    self.math=math

  @property
  def average_new(self):
    return str((self.phy+self.chem+self.math)/3)+"%"
  
stud_1=student(94,90,99)    
stud_1.chem=92
print(stud_1.chem)    
print(stud_1.average_new)  #we need't to call extra
