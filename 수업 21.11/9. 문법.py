
'''
A + B
'''
# a, b = map(int, input().split(' '))
# print(a + b)
# split: ''안에 있는 문자 기준으로 두동강


'''
A - B
'''
# a, b = map(int, input().split(' '))
# print(a - b)


'''
소수 찾기(x)
'''
# import random
#
# n = int(input())
# d = list(map(int, input().split(' ')))
#
# count = 0
#
# for i in range(len(d)):
#     elm = d[i]
#     flag = 1
#     for e in range(2, elm//2 + 1):
#         if elm % e == 0:
#             flag += 1
#             if flag >= 3:
#                 break
#     if flag == 2:
#         count += 1
#
# print(count)


'''
최소, 최대 10818
'''
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

# n = int(input())
# d = list(map(int, input().split(' ')))
# maximum_index = 0
# minimum_index = 0
# for i in range(len(d)):
#     if d[minimum_index] > d[i]:
#         minimum_index = i
#     if d[maximum_index] < d[i]:
#         maximum_index = i
# print(d[minimum_index], d[maximum_index])



