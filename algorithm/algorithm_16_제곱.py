a, n = map(int, input().split(' '))
b, s = map(int, input().split(' '))

answer_one = a
answer_two = b

for e in range(n-1):
    answer_one *= a
print(answer_one)

for i in range(s-1):
    answer_two *= b
print(answer_two)

sign = 0

if answer_one > answer_two:
    sign = ">"
if answer_one < answer_two:
    sign = "<"
if answer_one == answer_two:
    sign = "="

print(answer_one, sign, answer_two)

