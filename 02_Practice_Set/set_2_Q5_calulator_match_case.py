a=int(input("Enter a number 1:"))
b=int(input("Enter a number 2:"))
operator=input("Enter a  mentioned operator (+,_,*,/) :")

match operator :
   case "+" :
      print("a+b =",a+b)
   case "-" :
      print("a-b =",a-b)
   case "*" :
      print("a*b =",a*b)
   case "/" :
      print("a/b =",a/b)
