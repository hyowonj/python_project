'''
틱택토
'''
import random

# 틱택토 맵 만들기
def make_map():
    tic_map = []
    for i in range(9):
        tic_map.append(" ")
    return tic_map

def print_map(tic_map):
    print("----------")
    print(tic_map[0], "|", tic_map[1], "|", tic_map[2])
    print("----------")
    print(tic_map[3], "|", tic_map[4], "|", tic_map[5])
    print("----------")
    print(tic_map[6], "|", tic_map[7], "|", tic_map[8])
    print("----------")

tic_map = make_map()

# 플레이어는 먼저 말을 둘지 나중에 말을 둘지 선택할 수 있게 된다.
print("x를 선택하려면 1, o를 선택하려면 2를 입력해 주세요: ")
order = int(input())
block_num = 9
print("총 9개의 칸이 있습니다. 9개 칸 중 가장 왼쪽 위에 있는 칸은 0번, 가장 오른쪽 아래 있는 칸은 8번 입니다.")
print(print_map(tic_map))

while True:

    # 플레이어 선, 컴퓨터 후
    if order == 1:
        a = "x"
        b = "o"
        player_1 = int(input("x를 놓을 칸을 입력해 주세요: "))
        if tic_map[player_1] == " ":
            tic_map[player_1] = "x"
            print("플레이어: {}".format(player_1))
            block_num -= 1
            computer = random.randrange(9)
            if block_num == 0:
                print(print_map(tic_map))
                break
            else:
                while True:
                    if tic_map[computer] == " ":
                        tic_map[computer] = "o"
                        print("컴퓨터: {}".format(computer))
                        print(print_map(tic_map))
                        block_num -= 1
                        break
                    else:
                        computer = random.randrange(9)
        else:
            print("try again")

    # 컴퓨터 선, 플레이어 후
    if order == 2:
        a = "o"
        b = "x"
        computer = random.randrange(9)
        while True:
            if tic_map[computer] == " ":
                tic_map[computer] = "x"
                print("컴퓨터: {}".format(computer))
                print(print_map(tic_map))
                block_num -= 1
                if block_num == 0:
                    print(print_map(tic_map))
                    break
                else:
                    player_2 = int(input("o를 놓을 칸을 입력해 주세요: "))
                    while True:
                        if tic_map[player_2] != " ":
                            player_2 = int(input("o를 놓을 칸을 입력해 주세요: "))
                        else:
                            tic_map[player_2] = "o"
                            print("플레이어: {}".format(player_2))
                            block_num -= 1
                            print(print_map(tic_map))
                            break
            else:
                computer = random.randrange(9)

    # 승부확인
    if tic_map[0] == a and tic_map[1] == a and tic_map[2] == a:
        print("you win")
        break
    if tic_map[3] == a and tic_map[4] == a and tic_map[5] == a:
        print("you win")
        break
    if tic_map[6] == a and tic_map[7] == a and tic_map[8] == a:
        print("you win")
        break
    if tic_map[0] == a and tic_map[4] == a and tic_map[8] == a:
        print("you win")
        break
    if tic_map[2] == a and tic_map[4] == a and tic_map[6] == a:
        print("you win")
        break
    if tic_map[0] == b and tic_map[1] == b and tic_map[2] == b:
        print("you lose")
        break
    if tic_map[3] == b and tic_map[4] == b and tic_map[5] == b:
        print("you lose")
        break
    if tic_map[6] == b and tic_map[7] == b and tic_map[8] == b:
        print("you lose")
        break
    if tic_map[0] == b and tic_map[4] == b and tic_map[8] == b:
        print("you lose")
        break
    if tic_map[2] == b and tic_map[4] == b and tic_map[6] == b:
        print("you lose")
        break
