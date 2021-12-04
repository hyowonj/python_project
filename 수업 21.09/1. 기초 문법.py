# a=8 #a:int(정수)변수
# b="dd"#str(string)문자
# ""있으면 string ex)"4"도 문자
# c=3.5 #float소수
# print(a)
# print(b)

# 계산:+-/*% # %:분자
# print(9%5)
# print(type(3))
# print(type("dd"))
# print(type(3.4))
# 0:false 1:true

# d=True #bool(T or F)대문자 유의
# print(type(d))

# e=5
# if e!=6:   #<(작다) >(크다) ==(같다) !=(같지 않다) <=(크지 않다) >=(작지 읺다)
#     print(e)

# a=int(input())
# b="홀수"
# c="짝수"
# if a%2==0:
#     print(c)
# if a%2!=0:
#     print(b)

# e=int(input()) #input->문자 int(input())->숫자
# print(e)
# for d in range(10):
#     print(d)
# for e in range(1,11):
#     print("*"*e)
# for e in range(1,11):
#     print("*"*(11-e))


# f=int(input())
# h=7
# for g in range(2,f):
#     if f%g==0:
#         h=h+1
#     if f%g!=0:
#         h=h
# if h!=7:
#     print("소수가 아니다")
# if h==7:
#     print("소수이다")


# for i in range(1,11):
#     print("*"*(11-i))
# for i in range(1,11):
#     print("*"*i)
#
# a=5
# if a!=6:
#     print("haha")
# print("hihi")

# b=9
# if b==9:
#     print("yay")
# if b==8:
#     print("123")
# else:
#     print("0w0")

# d=int(input())
# f=1
# for c in range (2,d):
#     if d%c==0:
#         f=f+1
#     else:
#         f=f
# if f!=1:
#     print("소수가 아니다")
# else:
#     print("소수이다")
#
# for h in range(10):
#     if h==5:
#         continue
#     print(h)

# import random
# random.randrange(1,7)
# h=random.randrange(1,7)
# print(h)

# a=[1,2]
# print(a)
# a.append(7)
# print(a)
# print(a[0])

# i=0
# while i < 10:
#     print("hi",i)
#     i=i+1

# a=0
# while a < 10:
#     print("*"*(a+1))
#     a=a+1

# for i in range (1,100):
#
#     one = i % 10
#     ten = i // 10
#     first_if = one % 3 == 0 and one != 0
#     second_if = ten % 3 == 0 and ten !=0
#
#     if first_if and second_if:
#         print("**")
#     elif first_if or second_if:
#         print("*")
#     else:
#         print(i)
