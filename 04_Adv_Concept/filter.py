def is_grater_than_0(x):
  if x>0:
    return True
  else :
    return False
  
num=[2,-5,0,6,-9,5,9]
new = filter(is_grater_than_0,num)  #only filter number is show,whenever function is true
print(list(new)) 
print(list(filter(lambda x:x>0,num)))