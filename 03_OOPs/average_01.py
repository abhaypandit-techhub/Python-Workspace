class student :
  # def __init__(self,name,sub_1,sub_2,sub_3):
    # self.name=name
    # self.sub_1=sub_1
    # self.sub_2=sub_2
    # self.sub_3=sub_3
    # best way to creating upper instance,mentioned below
  def __init__(self,name,marks) :
    self.name=name
    self.marks=marks

  def average(self):
    sum=0
    for value in self.marks :
      sum+=value
    return sum/3
  
s1=student("abhay",[90,85,96])

print(s1.name)
print("Average of thre subject is ",s1.average(),"%")
