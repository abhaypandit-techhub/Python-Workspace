age=int(input("Enter your age:"))

if(age==0):
  print("you are born")

elif (age<18): # it is also correct "elif age<18 :"
  print("Your are a minor")
  
elif(age==18):
  print("You just become adult")

else:
  print("you are adult")

print("End of program") #outside the if statement
