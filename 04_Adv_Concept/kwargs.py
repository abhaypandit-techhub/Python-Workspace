# WAY-1

def marks(**kwargs):
  for item in kwargs.keys():
    print(f"The marks of {item} are {kwargs[item]}")

marks(abhay=67,kunal=90,alok=89)

# WAY-2
print("Next Part")

def marks(**kwargs):
  for item,score in kwargs.items():
    print(f"The marks of {item} are {score}")

marks(aniket=77,sachin=80,ratan=99)