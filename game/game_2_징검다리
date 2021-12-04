'''
징검다리
'''
import random
print("13개의 다리를 건너세요. 총 8번의 찬스가 있습니다. 오른쪽으로 가려면 1번, 왼쪽으로 가려면 2번을 입력하세요.")

chance = 8
bridge = 13
while chance > 0 and bridge > 0:

    a = int(input())
    b = random.randrange(1, 3)

    if a!= b:
        chance -= 1
        print("당신은 죽었습니다. 당신은 찬스를 써서 다시 살아났습니다. 남은 다리: {}, 남은 찬스: {}".format(bridge,chance))

    if a == b:
        bridge -= 1
        print("당신은 죽지 않았습니다. 남은 다리: {}, 남은 찬스: {}".format(bridge,chance))

if bridge == 0:
    print("당신은 최종 우승자임")
