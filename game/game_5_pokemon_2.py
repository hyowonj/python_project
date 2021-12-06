'''
포켓몬 업그레이드
'''
import random

class makeCh():
    # 플레이어와 컴퓨터의 에너지와 능력치, 플레이어의 에너지는 컴퓨터보다 낮게 시작한다.
    def __init__(self):
        self.p_hp = random.randrange(145, 160)
        self.mp = random.randrange(100, 140)
        self.c_hp = random.randrange(200, 225)

    # 약한 공격
    def s_damage(self):
        return self.p_hp * 0.1
        return self.c_hp * 0.15

    # 강한 공격
    def b_damage(self):
        return self.p_hp * (random.randrange(3, 7) / 10)
        return self.c_hp * (random.randrange(4, 7) / 10)

player = makeCh()
print("player --- hp: {}, mp: {}".format(player.p_hp, player.mp))

computer = makeCh()
print("computer --- hp: {}, mp: {}".format(computer.c_hp, computer.mp))

# 플레이어는 매 라운드가 시작될 때 마다 자신의 능력치와 에너지 중 하나를 선택해 회복할 수 있게 된다.
def player_chance():

    player_skill = int(input("if you select 1, you can get 10 more mp, and if you select 2, you can add 15 more hp."))
    if player_skill == 1:
        player.mp += 10
        print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))
    if player_skill == 2:
        player.p_hp += 15
        print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))

def turn_player():
    # 플레이어는 컴퓨터에게 약한 공격을 입힐지 강한 공격을 입힐지 선택할 수 있게 된다.
    player_select = int(input("select small_damage(1) or big_damage(2)"))

    if player_select == 1:
        print("player: small damage to computer")
        computer.c_hp = computer.c_hp - player.s_damage()
        print("computer >>> hp: {}, mp: {}".format(computer.c_hp, computer.mp))

    if player_select == 2:
        if player.mp - 40 >= 0:
            print("player: big damage to computer")
            computer.c_hp = computer.c_hp - player.b_damage()
            player.mp -= 40
            print("computer >>> hp: {}, mp: {}".format(computer.c_hp, computer.mp))
        else:
            print("you don't have enough mp to use this skill, you can only use skill(1) from now on")
    if player_select != 1 and player_select != 2:
        print("you don't have any skill beside skill(1) and skill(2), now your turn goes to computer")


def turn_computer():
    # 컴퓨터는 랜덤으로 플레이어에게 약한 공격이나 강한 공격을 입힐 수 있다.
    computer_select = random.randrange(1, 3)

    if computer_select == 1:
        print("computer: small damage to player")
        player.p_hp = player.p_hp - computer.s_damage()
        print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))
        print("player --- hp: {}, mp: {}".format(player.p_hp, player.mp))
        print("computer --- hp: {}, mp: {}".format(computer.c_hp, computer.mp))

    if computer_select == 2:
        if computer.mp - 40 >= 0:
            print("computer: big damage to player")
            player.p_hp = player.p_hp - computer.b_damage()
            computer.mp -= 40
            print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))
            print("player --- hp: {}, mp: {}".format(player.p_hp, player.mp))
            print("computer --- hp: {}, mp: {}".format(computer.c_hp, computer.mp))
        else:
            print("computer: small damage to player")
            player.p_hp = player.p_hp - computer.s_damage()
            print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))
            print("player --- hp: {}, mp: {}".format(player.p_hp, player.mp))
            print("computer --- hp: {}, mp: {}".format(computer.c_hp, computer.mp))

# 플레이어에게 먼저 공격하거나 나중에 공격할 수 있는 선택권이 쥐어진다
order = int(input("you wanna go first(1) or second(2)?"))

while player.p_hp > 0 and computer.c_hp > 0:

    if order == 1:
        print(player_chance())
        print(turn_player())
        print(turn_computer())

    if order == 2:
        print(player_chance())
        print(turn_computer())
        print(turn_player())

# 플레이어의 에너지가 먼저 0이하로 되면 플레이어가 지게 된다.
if player.p_hp <= 0:
    print("-------you lose-------")

# 컴퓨터의 에너지가 먼저 0이하로 되면 플레이어가 이기게 된다.
elif computer.c_hp <= 0:
    print("-------you win--------")
