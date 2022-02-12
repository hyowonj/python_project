# 1016번 (미완성)

a, b = map(int, input().split(' '))
squared = 0
for i in range(a, b):
    for e in range(b):
        if i == e*e:
            squared += 1

c = b - a
print(c - squared)
