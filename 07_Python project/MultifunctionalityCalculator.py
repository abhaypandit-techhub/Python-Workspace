import math

def calculator():
    
      while True:
        print("\n(A) Press '1' for add, sub, mult, div, exponent")
        print("(B) Press '2' for factorial")
        print("(C) Press '3' for log")
        print("(D) Press '4' for Trigonometric")
        print("(E) Press '5' for Exponential")
        print("(F) Press '6' for square root")
        print("(G) Press '7' for Temperature Conversion (Fahrenheit, Celsius, Kelvin)")
        print("(H) Press '8' for unit Conversion (mm,cm,dm,m,dam,hm,km)")

        num = int(input("\nPRESS A NUMBER : "))
        if num not in range(1,9):
          print("Wrong Press")
        else:
         
# ARITHMETIC Operation

         if num == 1:


            print("\n(A) '+' for Addition\n(B) '-' for Subtraction\n(C) '*' for Multiplication\n(D) '/' for Division\n(E) '**' for Exponential")
            operator = input("Enter operator (+,-,*,/,**) : ")
           
            if operator not in ["+","-","*","/","**"]:
                print("Invalid operator")
            else:
                a = int(input("\nEnter a value of a: "))
                b = int(input("Enter a value of b: "))

            match operator:
                case "+": print("a+b =", a+b)
                case "-": print("a-b =", a-b)
                case "*": print("a*b =", a*b)
                case "/": print("a/b =", "Can't divide by 0" if b==0 else a/b)
                case "**": print("a^b =", a**b)
                case _: print("Error")

# FACTORAIAL
         elif num == 2:
            a = int(input("\nEnter a number : "))
            print("factorial of", a, "is", math.factorial(a))

# log
         elif num == 3:
            base = int(input("Enter base of log : "))
            numb = int(input("Enter number for log : "))
            if base <= 0 or base == 1:
                print("Base must be greater than 0 and not equal to 1")
            elif numb <= 0:
                print("Number must be greater than 0")
            else:
             print(f"log({numb},{base}) =", math.log(numb, base))

# Trigonometric values

         elif num == 4:
                    
                    print("(A) Press '1' for sin\n(B) Press '2' for cos\n(C) Press '3' for tan\n(D) Press '4' for cot\n(E) Press '5' for sec\n(F) Press '6' for cosec")
                    
                    try :
                         
     
                         print("\nChoose trigonometric function")
                         choice = int(input("Enter choice : "))
                         if choice not in range(1,8):
                              print("Wrong choice")
                       
                         angle = int(input("Enter angle in degrees : "))
                         rad = math.radians(angle)
                         if choice == 1: print(f"sin{angle} =", math.sin(rad))
                         elif choice == 2: print(f"cos{angle} =", math.cos(rad))
                         elif choice == 3: print(f"tan{angle} =", math.tan(rad))
                         elif choice == 4: print(f"cot{angle} =", 1/math.tan(rad))
                         elif choice == 5: print(f"sec{angle} =", 1/math.cos(rad))
                         elif choice == 6: print(f"cosec{angle} =", 1/math.sin(rad))
                         
                    except Exception as e :
                         print(e)
          
# Exponential

         elif num == 5:

            x = int(input("Enter exponent power: "))
            print(f"e^{x} =", math.exp(x))

# Square root

         elif num == 6:

            x = int(input("Enter a number : "))
            if x<0:
                print("Can't calculate square root of negative number")
            print(f"√{x} =", math.sqrt(x))

# Temperature Conversion

         elif num == 7:


            print("\nTemperature Conversion")
            print("1: Fahrenheit → Celsius")
            print("2: Celsius → Fahrenheit")
            print("3: Kelvin → Celsius")
            print("4: Celsius → Kelvin")

            choice = int(input("Press a number : "))
            if choice not in range(1,5):
                print("Invalid choice")
            else:
                                   
              if choice == 1:
                F = float(input("°F = "))
                print("°C =", (5/9)*(F-32))
              elif choice == 2:
                C = float(input("°C = "))
                print("°F =", (9/5)*C+32)
              elif choice == 3:
                K = float(input("Kelvin = "))
                print("°C =", K-273.15)
              elif choice == 4:
                C = float(input("Celsius = "))
                print("K =", C+273.15)

# Unit Conversion
         elif num==8:
            

            print("\n(A) Press '1' for km\n(B) Press '2' for hm\n(C) Press '3' for dam\n(D) Press '4' for m\n(E) Press '5' for dm\n(F) Press '6' for cm\n(G) Press '7' for mm")
            list_1=["km","hm","dam","m","dm","cm","mm"]
            index_1=int(input("Press a first unit : "))
            if index_1 not in range(1,8):
                print("Invalid choice")

            print("(A) Press '1' for km\n(B) Press '2' for hm\n(C) Press '3' for dam\n(D) Press '4' for m\n(E) Press '5' for dm\n(F) Press '6' for cm\n(G) Press '7' for mm")
            list_2=["km","hm","dam","m","dm","cm","mm"]
            index_2=int(input("Press a second unit : "))

            if index_2 not in range(1,8):
                print("Invalid choice")
            else:

              value=float(input("Enter a number: "))
              Exponents=index_2-index_1
              result=(value*(10**Exponents))

              print(list_1[index_1-1] ,"-", list_2[index_2-1])
              print(result,list_2[index_2-1])
            
calculator()