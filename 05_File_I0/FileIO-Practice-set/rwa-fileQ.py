# Write mode in file
with open("tasks.txt","w") as f:

  bio="""GOOD MORNING TO EVERYONE!
I AM ABHAY."""
  f.write(bio)

# Append Task is Complted! in file tasks.txt
with open("tasks.txt","a") as f:
  bio1="\nTask is completed!"
  f.write(bio1)

# readline in list
with open("tasks.txt",'r') as f:
  for line in f.readlines():
    # print(line) 
# extra whitespace character comes so to remove use strip() function
    print(line.strip())