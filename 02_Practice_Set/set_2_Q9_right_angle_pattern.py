#Methode-1

for i in range (1,5) :
      print("*"*i)
        

#Method-2

for i in range (1,5) :
      for j in range (1,i+1) :
            # for j in range (0,i) :
            # for j in range (i) : # all meaning same thing
            print("*",end=" ")
      print(" ")
