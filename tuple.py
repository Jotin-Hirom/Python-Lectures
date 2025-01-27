tuple = tuple([2,3,4])
print(tuple)

tuple = "Jotin",21,"24-10-2001","BCA"
name,*age,course = tuple
print(name)
print(age)
print(course)
print()
print()

import sys
list = ["Jotin", 21, "BCA"]
tuple = ("Jotin", 21, "BCA")
dict = {"Jotin", 21, "BCA"}
print(sys.getsizeof(list), "bytes")
print(sys.getsizeof(tuple), "bytes") 
print(sys.getsizeof(dict), "bytes")

import sys
list = ["Jotin", 21, "BCA"]
tuple = ("Jotin", 21, "BCA")
dict = {"Jotin", 21, "BCA"}
print(sys.getsizeof(list), "bytes")
print(sys.getsizeof(tuple), "bytes")
print(sys.getsizeof(dict), "bytes")

import timeit as t
print(t.timeit(stmt="[1,2,3,4]",number=100000))
print(t.timeit(stmt="(1,2,3,4)",number=100000)) 
print(t.timeit(stmt="{1:1,2:2,3:3,4:4}",number=100000)) 