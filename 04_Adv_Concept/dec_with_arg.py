# Decorators with argument
def repeat(n):
  def decorator(func):
    def wrapper(a):
      for i in range(n):
         func(a) # it call the say_Byy function
    return wrapper # decorator return wrapper function
  return decorator      
@repeat(5) 
def say_Byy(a):
  print(f"Hi, {a}")
say_Byy("Abahy")

# EXECUTION FROM WHEN WE CALLED THE FUNCTION