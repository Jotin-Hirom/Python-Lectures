mydict = {"name":"Jotin", "age":21, "course":"BCA"}
# dict_copy = mydict.copy()
dict_copy = dict(mydict)
dict_copy["address"] = "Heingang"
print(dict_copy)
print(mydict)
dict_1 = dict(name="Inaoba")
mydict.update(dict_1)
print(mydict)

for i,j in mydict.items():
    print(i, j) 