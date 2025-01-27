# from itertools import product
# a = [1,2]
# b = [3,4]
# prod = product(a,b) #Cartesian product
# print(list(prod))


# from itertools import permutations
# a = [1,2,3]
# prod = permutations(a,2) 
# print(list(prod))

# from itertools import combinations
# a = [1,2,3]
# prod = combinations(a,2) 
# print(list(prod))


# from itertools import combinations_with_replacement
# a = [1,2,3,4]
# prod = combinations_with_replacement(a,2) 
# print(list(prod))


# from itertools import accumulate
# import operator
# a = [1,2,3,4]
# prod = accumulate(a,func=operator.mul) 
# print(list(prod))


# from itertools import groupby
# a = [1,2,3,4]
# def smaller_than_3(x):
#     return x<3
# prod = groupby(a,smaller_than_3) 
# for k, v in prod:
#     print(k,list(v))
# prod = groupby(a,lambda x: x<4) 
# for k, v in prod:
#     print(k,list(v))
# person = [{"name":"John", "age":56},{"name":"Danny", "age":50},{"name":"Saber", "age":45}]
# prod = groupby(person,lambda x: x["age"]<50) 
# for k, v in prod:
#     print(k,list(v))

# from itertools import count, cycle, repeat, pairwise
# for i in count(10):
#     print(i)
#     if i == 15:
#         break
# a = [1,2,3,4]
# for i in cycle(a):
#     print(i)
#     if i==4:
#         break
# for i in repeat(a,7):
#     print(i)

# from itertools import pairwise
# a = [1,2,3,4]
# prod = pairwise(a) 
# print(list(prod))


from itertools import zip_longest
a = [1,2,3,4]
prod = zip_longest(a,{1,2,3,4}) 
print(list(prod))