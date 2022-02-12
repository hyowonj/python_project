# 2161번

N = int(input())
lst = []
answer = [1]
for i in range(1, N + 1):
    lst.append(i)
while len(lst) != 1:
    del lst[0]
    for j in range(len(lst)-1):
        lst[j], lst[j + 1] = lst[j + 1], lst[j]
    answer.append(lst[0])
for e in answer:
    print(e, end= " ")
