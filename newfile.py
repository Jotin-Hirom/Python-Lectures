testSize = int(input())
nArr=[]
for i in range(1,testSize+1):
    nArr.append(int(input()))
  
for n in nArr:
    if n>=1 and n<=(10**9):
        prod = 1
        sum = 0
        for i in range(1, n+1):
            prod = prod*i
            sum = sum+i
        if prod%sum==0:
            print("YEAH")
        else:
            print("NAH")


data  = input()
li = data.split()
   
a = int(li[0])
b = int(li[1])
   
def gcd(a, b):
    if (a == 0): 
        return b; 
    return gcd(b%a, a); 
   
if (a>0 and a<(10**12+1) and b>=1 and b<(10**12+1)):
    count = 1
    for i in range(2, gcd(a, b)+1):
        if a%i==0 and b%i==0:
            count = count+1
    print(count)



msg = " ababacd"
li = [0] * 26
print(f"Origional string: {msg}")
out= ""
for ch in msg:
    ind = ord(ch) - ord('a')
    if li[ind] == 0:
        out=out+ch
        li[ind] = 1

print(f"Unique characters in string: {out}")