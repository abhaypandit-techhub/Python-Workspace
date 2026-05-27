data={"abhay":45,"alok":50}
print(data,type(data))
print(data["alok"])
data["abhay"]=49
print(data)
print(data.keys())
print(data.values())#print key value
print(data.clear())#clear dictionary

#Dictionary comprehension
table={i:5*i for i in range (1,11)}
square={i:i*i for i in range (1,11)}
print(table)
print(square)