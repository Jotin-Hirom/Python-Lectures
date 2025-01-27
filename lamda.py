# add10 = lambda x: x+10
# multi = lambda x,y: x*y
# print(add10(10))
# print(multi(10,8))

# data = [(1, 1), (2, -2), (-3, 3), (4, -4)]
# data__sorted = sorted(data)
# def sorting(x):
#     return x[1]
# data__sorted = sorted(data, key=sorting)
# data__sorted1 = sorted(data, key=lambda x: x[1],reverse=True)
# data__sorted2 = sorted(data, key=lambda x: x[1]+x[0])
# print(data__sorted1)
# print(data__sorted)
# print(data__sorted2)

# map(func,iterable)
a = [1,2,3,4,5,6,7,8,9,10]
# b = map(lambda x: x*2, a)
# b = [i*2 for i in a]
# print(list(b))

# b = filter(lambda x: x%2==0, a)
# b1 = [i for i in a if i%2==0]
# print(list(b))
# print(list(b1))

import functools as f
b = f.reduce(lambda x,y: x+y, a)
print(b)

