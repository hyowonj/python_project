# 2576번

q = int(input())
w = int(input())
e = int(input())
r = int(input())
t = int(input())
y = int(input())
u = int(input())

list = [q, w, e, r, t, y, u]
odd_list = []
odd = 0

for i in range(7):
    if list[i] % 2 != 0:
        odd += list[i]
        odd_list.append(list[i])
if len(odd_list) != 0:
    print(odd)
    min = odd_list[0]
    for e in range(len(odd_list)):
        if min > odd_list[e]:
            min = odd_list[e]
    print(min)
else:
    print("-1")
