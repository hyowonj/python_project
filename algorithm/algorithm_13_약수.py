a = int(input())
list = list(map(int, input().split(' ')))

b = 0
s = 0
for i in range(len(list)):
    if list[s] > list[i]:
        s = i
    if list[b] < list[i]:
        b = i
print(list[s] * list[b])
