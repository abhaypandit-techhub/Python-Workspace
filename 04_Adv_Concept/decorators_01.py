def decorator(func):#decorators takes a function and create a new function wrapper
  def wrapper(): 

    '''Wrapper = ek function jo kisi dusre function ko “wrap” (ghere / cover) karta hai
👉 Matlab:
Pehle kuch extra kaam karega
Fir original function ko call karega'''

    print("ready to execeute a function")
    print("now i am executed this function...")
    func()
  return wrapper  #this return belong to decorator
@decorator  #it simply mean internally say_Byy = decorator(say_Byy) ,say hello now become a wrapper function
#Code zyada clean + readable
def say_Byy():
  print("Byy")
say_Byy() 
# x=decorator(say_Byy)
# x() #Now x will be a new function
'''instead of you writing
 x=decorator(say_Byy)
 x()
 we replace to  @decorator'''
'''x will be look like
def x()
    print("now i am executed this function...")
     print("Byy") 
    print("ready to execeute a function")
'''