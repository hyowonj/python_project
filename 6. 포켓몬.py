# class makeA():
#     def print_test(self):
#         print("bye")
#
# a = makeA()
# a.print_test()

'''
포켓몬...?
'''
# import random
#
# class makeCh(): # 앞에 소문자 뒤에 대문자
#
#     def __init__(self): # 언더 바 두개: __.__ 기능
#         self.hp = random.randrange(200, 300)
#         self.mp = random.randrange(60, 100)
#
#     def s_damage(self):
#         return self.hp * 0.1
#
#     def b_damage(self):
#         return self.hp * 0.3
#
# player = makeCh()
# print("player --- hp: {}, mp: {}".format(player.hp, player.mp))
#
# computer = makeCh()
# print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))
#
# while player.hp > 0 and computer.hp > 0:
#
#     player_select = int(input("select small_damage(1) or big_damage(2)"))
#
#     if player_select == 1:
#         print("player: small damage to computer")
#         computer.hp = computer.hp - player.s_damage()
#         print("computer >>> hp: {}, mp: {}".format(computer.hp, computer.mp))
#
#     if player_select == 2:
#         if player.mp - 30 >= 0:
#             print("player: big damage to computer")
#             computer.hp = computer.hp - player.b_damage()
#             player.mp -= 30
#             print("computer >>> hp: {}, mp: {}".format(computer.hp, computer.mp))
#         else:
#             print("you don't have enough mp to use this skill")
#
#     computer_select = random.randrange(1, 3)
#
#     if computer_select == 1:
#         print("computer: small damage to player")
#         player.hp = player.hp - computer.s_damage()
#         print("player >>> hp: {}, mp: {}".format(player.hp, player.mp))
#         print("player --- hp: {}, mp: {}".format(player.hp, player.mp))
#         print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))
#
#     if computer_select == 2:
#         if computer.mp - 30 >= 0:
#             print("computer: big damage to player")
#             player.hp = player.hp - computer.b_damage()
#             computer.mp -= 30
#             print("player >>> hp: {}, mp: {}".format(player.hp, player.mp))
#             print("player --- hp: {}, mp: {}".format(player.hp, player.mp))
#             print("computer --- hp: {}, mp: {}".format(computer.hp, computer.mp))
#         else:
#             computer_select = random.randrange(1, 2)
#
#     if player.hp <= 0:
#         print("you lose")
#
#     if computer.hp <= 0:
#         print("you win")


# dictionary
# a = {}
# a['hi'] = 'hihihi'
# a['bye'] = 'byeee'
# print(a['hi'])
# print(a['bye'])

'''
포켓몬 업그레이드
'''
import random

class makeCh():

    def __init__(self):
        self.p_hp = random.randrange(150, 175)
        self.mp = random.randrange(100, 140)
        self.c_hp = random.randrange(200, 225)

    def s_damage(self):
        return self.p_hp * 0.1
        return self.c_hp * 0.15

    def b_damage(self):
        return self.p_hp * (random.randrange(3, 7) / 10)
        return self.c_hp * (random.randrange(2, 6) / 10)

player = makeCh()
print("player --- hp: {}, mp: {}".format(player.p_hp, player.mp))

computer = makeCh()
print("computer --- hp: {}, mp: {}".format(computer.c_hp, computer.mp))

def player_chance():

    player_skill = int(input("if you select 1, you can get 10 more mp, and if you select 2, you can add 15 more hp."))
    if player_skill == 1:
        player.mp += 10
        print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))
    if player_skill == 2:
        player.p_hp += 15
        print("player >>> hp: {}, mp: {}".format(player.p_hp, player.mp))

def turn_player():

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

if player.p_hp <= 0:
    print("-------you lose-------")

elif computer.c_hp <= 0:
    print("-------you win--------")