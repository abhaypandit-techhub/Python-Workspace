
#method-1

n=123
sum=0
while n>0 :
  rem=n%10
  sum=sum*10 + rem
  n=n//10
print("The reverse of the number 123 is",sum)

#Method-2
num=4255
print(int(str(num)[::-1]))