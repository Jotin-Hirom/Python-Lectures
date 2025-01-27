import json 

person = {
    "name" : "Jotin Hirom",
    "standard" : "Post Graduate",
    "blind" : False,
    "hobbies" : ["lala", "dada"],
    "names" : [{"first":"Jotin"},{"last":"Hirom"}]
}
# serialization
personData = json.dumps(person,indent=4,sort_keys=True,separators=(" , "," = "))
personData = json.dumps(person,indent=4,sort_keys=True)
print(personData)

# with open("JSON/person.json", '+w') as file:
#     json.dump(person, file, indent=4)

# de-serialization
# personDes = json.loads(personData)
# print(type(personDes))

# with open("JSON/person.json", "+r") as file:
#     data = json.load(file)
#     print(data)
# with open("example.json", "r") as file:
#     data = json.load(file)
#     dataJson = json.dumps(data)
#     length = len(dataJson)
#     # print(length)
#     print(dataJson["name"])
# i = 0
# while i < 5:
#     if i == 2 :
#         continue
#     else:
#         print(i, end = " ")
#         i+=1


