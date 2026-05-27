
#Q1 -- coversion

# coordinate=tuple(10*x for x in range(1,3))
# print(coordinate)
# print(coordinate[0])
# print(coordinate[1])
#coordinate[0]=50 #Not possible in tuple
#print(coordinate[0])
# coordinate=list(coordinate)
# coordinate.insert(0,50)
# print(coordinate)
# coordinate=tuple(coordinate)
# print(coordinate)

#Q2--set&set method

my_set={1,2,3,3,4}
print(my_set)
my_set.add(5)
print(my_set)
my_set.discard(2)
print(my_set)
a = 4 in my_set # check in 4 in my_set True/False output
print(a)

#Q3--set operation 
a={1,2,3}
b={3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
