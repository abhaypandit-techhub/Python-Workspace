def logger(func):
  def wrapper():
    print("Funtion is being called before called")
    func()
  return wrapper

@logger
def say_hello():
  print("Hello!")

say_hello()