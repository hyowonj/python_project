'''
로그인(완료x)
'''
# id_list=[]
# pwd_list=[]
# id= input()
# for e in range(5):
#     while True:
#         count = 0
#         temp_id = input("Enter your id: ")
#         for e in range(len(id_list)):
#             if id_list[e]==temp_id and len(id) < 8:
#                 count = 1
#             if count==0:
#                 print("ok")
#                 break
#         print("try another one")
#     id_list.append(temp_id)
#     temp_pwd=input("Enter your pwd: ")
#     pwd_list.append(temp_pwd)
#     print("You made it! id:{} pwd:{}".format(id_list,pwd_list))

# for a in range(1,10):
#     for b in range(1, 10):
#         print("{} x {} = {}".format(a,b,(a*b)))
# print("your id must be longer than 8")
# temp_id = input("Enter your id: ")
# if len(temp_id) < 8:
#     count = 1
#     print("your id must be longer than 8")
# else:
#     count = 0
# if count == 0:
#     print("ok")
#     temp_pwd = input("Enter your pwd: ")
# print("You made it! id:{} pwd:{}".format(temp_id, temp_pwd))


import random
a = []
def list_random():
    for i in range(10):
        b = random.randrange(1,100)
        a.append(b)
    return a


def searching_value(a):
    maximum_value = a[0]
    for i in range(len(a)):
        if maximum_value < a[i]:
            maximum_value = a[i]
    return maximum_value

temp_list = list_random()
result = searching_value(temp_list)










