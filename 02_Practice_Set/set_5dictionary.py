#Q1
# name={"Alice":"john","age":20,"grade":"A"}
# print(name.values())
# print(name["age"])

# name["grade"]="A+"
# print(name.values())

# name["city"]="Delhi"
# print(name)

#Q2

infor={
  "F_1":"Abhay","num_1":8825212414,
  "F_2":"Kunal","num_2":8822862586,
  "F_3":"Alok","num_3":8825212634
}
print(infor.keys())
print(infor.values())
for key,value in infor.items() :
  print(key,value)
