# # str = """hello \
# # world"""
# str = "   hello world  " 
# str = str.strip()
# print(str)


# from timeit import default_timer as T
# list = ["z"]* 5
# #bad 
# my_string = ""
# start = T()
# for i in list:
#     my_string +=i
# stop = T()
# print(my_string)
# print(stop - start)

# # good
# start = T()
# my_string = "".join(list)
# stop = T()
# print(my_string)
# print(stop - start)

pi = 3.1437638746
text1 = "Value of pi is %.2f" %pi
text2 = "Value of pi is {:.4f} and {}".format(pi,pi)
text3 = f"Value of pi is {round(pi,5)}"
print(text1)
print(text2)
print(text3)

