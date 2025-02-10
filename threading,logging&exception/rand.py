# import random
# a = random.random()
# a = random.uniform(1,10) # random float
# a = random.randint(1, 10) # random int this include the upper-bound 
# a = random.randrange(1,10) # random int this not include the upper-bound 
# a = random.normalvariate(0,1) # random float for mean and standard deviation used for statistic 
# a = random.shuffle([1,2,3]) # random float for mean and standard deviation used for statistic 
# print(a)
# pseudo number - reproducible number 
# my_list = [A]
# my_list = list("ABCDEFGH")
# print(random.choice(my_list)) 
# print(random.sample(my_list,3)) 
# print(random.choices(my_list,k=3)) 
# random.shuffle(my_list)
# print(my_list) 
# random.seed(1) 
# print(random.random( )) 
# print(random.randint(1,10 ))
# random.seed(2)
# print(random.random( ))
# print(random.randint(1,10 ))

# import secrets
# # it takes more time
# a = secrets.randbelow(10)
# print(a)
# a = secrets.randbits(4) #1111 - 15
# print(a)
# my_list = list("ABCDEFGH")
# a = secrets.choice(my_list) 
# print(a)

# import numpy as np

# # a = np.random.rand(3,3)
# # print(a)
# # a = np.random.randint(0,10,(3,3)) #10 excluded
# # print(a) 
# a = np.array([[1,2,3],[4,5,6],[7,8,9]]) 
# np.random.shuffle(a)
# print(a)

# np.random.seed(1)
# print(np.random.rand(3,3))
# np.random.seed(1) 
# print(np.random.rand(3,3))