import random

print("select!")
question = int(input("1.자리배치하기 2.모둠활동 조짜기"))
n = int(input("총인원 수가 몇명입니까?"))
student = []
overlab_check = []
for s in range(1, n+1):
    student.append(s)
    overlab_check.append(0)

if question == 1:
    print("[학번,자리]입니다")
    for e in range(n):
        while True:
            h = random.randrange(1, n+1)
            if h in overlab_check:
                h = random.randrange(1, n+1)
            else:
                overlab_check[e] = h
                break
        print(student[e], overlab_check[e])

if question == 2:
    team = int(input("몇 개의 모둠으로 나눌 것입니까?"))
    print("모둠 당 인원수:{}, 남은 인원:{}".format(n//team, n-n//team*team))
    for e in range(n):
        while True:
            h = random.randrange(1, n+1)
            if h in overlab_check:
                 h = random.randrange(1, n+1)
            else:
                overlab_check[e] = h
                break
    for i in range(team):
        a = []
        a = overlab_check[i*(n//team):i*(n//team)+n//team]
        a.sort()
        b = overlab_check[n//team*team:]
        b.sort()
        print("{}모둠: {}".format(i+1, a))
    print("남은 인원: {}".format(b))

