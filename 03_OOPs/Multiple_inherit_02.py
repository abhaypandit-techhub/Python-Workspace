
#MULTIPLE INHERITANCE

class A:
  # intro=print("Name")
  name="Abhay Pandit"

class B:
  # intro_1=print("Abhay Pandit")
  Trade="B.tech CSE(AI&ML)"

class C:
  print("Trade")# it is automatic call when object is created 
  PRN=250205241039

class All(A,B,C):
  # print("B.tech CSE(AI&ML)")
  end="thank you"

details=All()
# print(details.name)