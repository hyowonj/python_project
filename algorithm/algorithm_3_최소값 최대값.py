import random
a = []
for i in range(10):
    b= random.randrange(1, 110)
    a.append(b)

maximum_value = a[0]
for c in range(10):
    if maximum_value < a[c]:
        maximum_value = a[c]
print(a)
print("가장 큰 값: {}".format(maximum_value))

minimum_value = a[0]
for d in range(10):
    if minimum_value > a[d]:
        minimum_value = a[d]
print("가장 작은 값: {}".format(minimum_value))
