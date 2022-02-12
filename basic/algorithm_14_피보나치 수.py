# 2747번

a = int(input())
list = [1 for i in range(a)]

for i in range(2, a):
    list[i] = list[i - 2] + list[i - 1]

print(list[a-1])
