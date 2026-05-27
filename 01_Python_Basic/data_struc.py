
# list_1=[2,56,67]
# list_1[0]=3
# list_2=["abhay",7,3.6]
# print(list_1)
# print(list_1[0])
# print(list_2[0])
# print(list_2[0:2])

#score =[2,5,7,8]
# print(score.append(9)) return nothing 
#print(score) # correct way to use append()
#score.pop()
#print(score)

#creating a list of table of five 
#method-1
# a=5
# table=[]
# for i in range(1,11) :
#   table.append(5*i)

#print(table)

#method-2
table=[5*i for i in range(1,11)]
print(table)

#TUPLES

tuple=(2,4,56,7)
#tuple[1]=3#we cann't do in tuple
print(tuple[1])

tuple_1=(3,6,9,3)
a,b,c,d=tuple_1
print(a,b,c)
print(tuple_1.count(3))
print(tuple_1.index(6))
