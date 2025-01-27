from collections import Counter
data  = "aaaaaaddfdfdfdfgdertncbngkojhdghoijbmxvkbhdfiughcvkhjdggsdgshdgsdgkfjlgklffghfkghkfngdfuiegv"
counter = Counter(data)
print(counter)
# print(counter.most_common(2))
# # for i in counter.most_common(2):
# #     print(type(i))
# print(counter.most_common(2)[1][1])
# list_data = list(counter.elements())
# list_data1 = counter.total()
# list_data2 = counter.get("a")
# print(list_data)
# print(list_data1)
# print(list_data2)

# from collections import namedtuple
# Point = namedtuple("Point","x,y")
# d = Point(1,-9)
# print(d)
# print(d.x)
# print(d.y)
# Name = namedtuple("Names","Jotin Inaoba")
# n = Name("Hirom","Heingang")
# print(n)
# print(n.Jotin)
# print(n.Inaoba)

# from collections import defaultdict
# dict = defaultdict(int)
# dict["a"] = 1
# print(dict["b"])


from collections import deque
dict = deque()

dict.append(2)
dict.appendleft(3)
# print(dict)

dict.extend([3,4,5])
dict.extendleft([7,8,9])
# print(dict)

dict.rotate(-1)
print(dict)

dict.reverse()
print(dict)

dict.pop() 
dict.popleft()
print(dict)



