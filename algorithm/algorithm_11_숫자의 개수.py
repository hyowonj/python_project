k = [0 for e in range(10)]
a = int(input())
b = int(input())
c = int(input())
d = a * b * c
d = str(d)
count = 0
print(d)
# print(len(number))
for i in range(len(d)):
    num = int(d[i])
    k[num] = k[num] + 1
