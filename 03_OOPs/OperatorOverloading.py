class point :
  def __init__(self,x,y):
    self.x=x
    self.y=y
  # def sum(self,p) ://Need not write these function after operator overloading
  #   return point((self.x+p.x),(self.y+p.y))
  def new_point(self) :
    return f"x is {self.x} and y is {self.y}"
  def __add__(self,p):
    return point((self.x+p.x),(self.y+p.y))
p1=point(3,2)  
p2=point(6,3)  
# p=p1.sum(p2)#that mean sum(p1,p2) 
# p=p1+p2 we cannot simply do this without using __add__ function
p=p1+p2 #we overloaded the + operator by writing __add__ funtion
print(p.new_point())
