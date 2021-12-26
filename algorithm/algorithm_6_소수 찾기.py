# 1978번(미완성)

n = int(input())
d = map(int, input().split(' '))

num_count = 0

for i in d:
    flag = 0
    if i > 1:
        for e in range(2, i):
            if i % e == 0:
                flag += 1
        if flag == 0:
            num_count += 1

print(flag)
