money = int(input())
a = money // 500
b = (money - 500*a) // 100
c = (money - 500*a - 100*b) // 50
d = (money - 500*a - 100*b - 50*c) // 10
money_list = [500, 100, 50, 10]
change_list = [a, b, c, d]

for i in range(len(money_list)):
    if money >= money_list[i]:
        print(change_list[i], money_list[i])
