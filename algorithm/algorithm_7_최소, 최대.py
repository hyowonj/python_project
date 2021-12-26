# 10818번

# n = int(input())
# d = list(map(int, input().split(' ')))
# maximum_value = d[0]
# minimum_value = d[0]
# for i in range(len(d)):
#     if minimum_value > d[i]:
#         minimum_value = d[i]
#     if maximum_value < d[i]:
#         maximum_value = d[i]
# print(minimum_value, maximum_value)

n = int(input())
d = list(map(int, input().split(' ')))
maximum_index = 0
minimum_index = 0
for i in range(len(d)):
    if d[minimum_index] > d[i]:
        minimum_index = i
    if d[maximum_index] < d[i]:
        maximum_index = i
print(d[minimum_index], d[maximum_index])
