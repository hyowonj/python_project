a = int(input())
list = list(map(int, input().split(' ')))
max = 0
b = 0
for i in range(len(list)):
    if list[max] < list[i]:
        max = i

for e in range(len(list)):
    b += (list[e] / list[max]) * 100
print(b / len(list))
