#List ia a changeable and ordered data type that allows duplicate members.

# mylist = [9,2,3,5,6]
# new_list = sorted(mylist)
# print(mylist)
# print(new_list)

# # reverse
# mylist_new = mylist[::-1]
# print(mylist_new)
# print(mylist[-1::])

# list_data = [2,3,4]
# list_data_1 = list_data
# list_data_1.append(4)
# list_data_2 = list_data_1.copy()
# print(list_data_2)
# list_data_2.append(4)
# print(list_data)
# print(list_data_1)
# print(list_data_2)

# list_item = [1, 2, 3, 4]
# list_item = [i*i for i in list_item]
# print(list_item)


list_item = [1, 2, 3, 4, 5, 6, 7]
one,two,*three,four = list_item
print(one)
print(two)
print(three)
# print(5 in three)
# print(5 not in three)
# print(four) 