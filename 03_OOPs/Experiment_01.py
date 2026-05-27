class student :
  def __init__(self,name,roll,branch):
    self.name=name
    self.roll=roll
    self.branch=branch 

  def show(self):
    print(f"{self.name}\t{self.roll}\t{self.branch}")

stud_1=[]

#class size
size=int(input("Size of class : "))
for i in range(size) :
  name=input("Student : ")
  Roll=int(input("Roll : "))
  branch=input("Branch : ")
  s=student(name,Roll,branch)
  stud_1.append(s)

print("*****DATA*****")
print("Name\t\tRoll\t\tBranch") 

for s in stud_1 :
  s.show()
