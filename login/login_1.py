'''
로그인
'''
# 빈 리스트를 만든다.
id_list = []
pwd_list = []
# 아이디, 비번 총 5세트 만들기
for e in range(5):
    # 먼저 아이디 입력
    temp_id = input("Enter your id: ")
    while True:
        count = 0
        # 아이디가 8글자 이상인지 아닌지 판단
        if len(temp_id) < 8:
            temp_id = input("Enter your id: ")
        if len(temp_id) >= 8:
            # 아이디가 중복 되었는지 판단
            for e in range(len(id_list)):
                if id_list[e] == temp_id:
                    temp_id = input("Enter your id: ")
                    count = 1
            # 비밀번호 입력
            if count == 0:
                print("ok")
                temp_pwd = input("Enter your pwd: ")
                print("ok")
                id_list.append(temp_id)
                pwd_list.append(temp_pwd)
                break
    print("You made it!! id:{} pwd:{}".format(id_list, pwd_list))












