'''
포켓몬
'''
import random

class makeCh(): # 앞에 소문자 뒤에 대문자

    def __init__(self): # 언더 바 두개: __.__ 기능
        self.hp = random.randrange(200, 300)
        self.mp = random.randrange(60, 100)

    def s_damage(self):
        return self.hp * 0.1

    def b_damage(self):
        return self.hp * 0.3

player = makeCh()
print("player --- hp: {}, mp: {}".format(player.hp, player.mp))

computer = makeCh()
print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))

while player.hp > 0 and computer.hp > 0:

    player_select = int(input("select small_damage(1) or big_damage(2)"))

    if player_select == 1:
        print("player: small damage to computer")
        computer.hp = computer.hp - player.s_damage()
        print("computer >>> hp: {}, mp: {}".format(computer.hp, computer.mp))

    if player_select == 2:
        if player.mp - 30 >= 0:
            print("player: big damage to computer")
            computer.hp = computer.hp - player.b_damage()
            player.mp -= 30
            print("computer >>> hp: {}, mp: {}".format(computer.hp, computer.mp))
        else:
            print("you don't have enough mp to use this skill")

    computer_select = random.randrange(1, 3)

    if computer_select == 1:
        print("computer: small damage to player")
        player.hp = player.hp - computer.s_damage()
        print("player >>> hp: {}, mp: {}".format(player.hp, player.mp))
        print("player --- hp: {}, mp: {}".format(player.hp, player.mp))
        print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))

    if computer_select == 2:
        if computer.mp - 30 >= 0:
            print("computer: big damage to player")
            player.hp = player.hp - computer.b_damage()
            computer.mp -= 30
            print("player >>> hp: {}, mp: {}".format(player.hp, player.mp))
            print("player --- hp: {}, mp: {}".format(player.hp, player.mp))
            print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))
        else:
            computer_select = random.randrange(1, 2)

    if player.hp <= 0:
        print("you lose")

    if computer.hp <= 0:
        print("you win")



