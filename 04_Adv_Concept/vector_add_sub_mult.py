class vector :
  def __init__(self,x,y):
    self.x=x
    self.y=y

# for vector addition
  def __add__(self,value_1):
    print(f"v_1 = {self.x}i + {self.y}j\nv_2 = {value_1.x}i + {value_1.y}j")
    return f"v_1 + v_2 = {self.x + value_1.x}i + {self.y+value_1.y}j"
  
# for vector subtraction
  def __sub__(self,value_1):
    return f"v_1 - v_2 = {self.x-value_1.x}i + {self.y-value_1.y}j"
  
# for vector multiplication  
  def __mul__(self,value_1):
    return f"v_1*v_2 = {self.x*value_1.x}i + {self.y*value_1.y}j"

v_1=vector(4,6)
v_2=vector(3,7)

v_3 = v_1+v_2
print(v_3)

v_3 = v_1 -v_2
print(v_3)

v_3=v_1*v_2
print(v_3)
  