'''
가위바위보
'''
import random
print("1은 가위, 2는 바위, 3은 보자기")

player_coin = 600
computer_coin = 600
while player_coin > 0 and computer_coin > 0:

    a = random.randrange(1, 4)
    b = int(input())

    if a == b:
        print("컴퓨터: {}, 무승부".format(a))
        print("플레이어 코인: {}, 컴퓨터 코인: {}".format(player_coin, computer_coin))

    if b+1 == a or a-b == -2:
        print("컴퓨터: {}, 당신이 졌습니다. 플레이어 200코인 감소".format(a))
        print("플레이어 코인: {}, 컴퓨터 코인: {}".format(player_coin - 200, computer_coin + 200))
        player_coin = player_coin - 200
        computer_coin = computer_coin + 200
    if a+1 == b or a-b == 2:
        print("컴퓨터: {}, 당신이 이겼습니다. 플레이어 200코인 적립".format(a))
        print("플레이어 코인: {}, 컴퓨터 코인: {}".format(player_coin + 200, computer_coin - 200))
        player_coin += 200
        computer_coin -= 200

if player_coin == 0:
    print("당신이 졌습니다.")
elif player_coin == 1200:
    print("당신이 이겼습니다.")

