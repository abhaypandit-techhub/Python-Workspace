import argparse

parser=argparse.ArgumentParser(description="simple calculator")

# parser.add_argument("num1")
parser.add_argument("num1",type=float,help="First number")
parser.add_argument("num2",type=float,help="Second number")
parser.add_argument("operation",choices=["Add","Sub","Mul","Div"],help="Operation to perform")

args=parser.parse_args()
# print(args)
if(args.operation=="Add"):
  print(f"The result is {args.num1 + args.num2}")
elif(args.operation=="Sub"):
  print(f"The result is {args.num1 - args.num2}")
    
elif(args.operation=="Mul"):
  print(f"The result is {args.num1 * args.num2}")
    
elif(args.operation=="Div"):
  print(f"The result is {args.num1 / args.num2}")

else:
  print("Some error occured")  
    