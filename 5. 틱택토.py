'''
틱택토(미완성)
'''
# import random
#
# # 틱택토 맵 만들기
# def make_map():
#     tic_map = []
#     for i in range(9):
#         tic_map.append(0)
#     return tic_map
#
# def print_map(tic_map):
#     print("----------")
#     print(tic_map[0], "|", tic_map[1], "|", tic_map[2])
#     print("----------")
#     print(tic_map[3], "|", tic_map[4], "|", tic_map[5])
#     print("----------")
#     print(tic_map[6], "|", tic_map[7], "|", tic_map[8])
#     print("----------")
#
# # 승부 확인
# def check_win(tic_map, ab):
#     check_flag = 0
#     if tic_map[0] == ab and tic_map[1] == ab and tic_map[2] == ab:
#         check_flag = 1
#         print("win")
#     if tic_map[3] == ab and tic_map[4] == ab and tic_map[5] == ab:
#         check_flag = 1
#         print("win")
#     if tic_map[6] == ab and tic_map[7] == ab and tic_map[8] == ab:
#         check_flag = 1
#         print("win")
#     if tic_map[0] == ab and tic_map[4] == ab and tic_map[8] == ab:
#         check_flag = 1
#         print("win")
#     if tic_map[2] == ab and tic_map[4] == ab and tic_map[6] == ab:
#         check_flag = 1
#         print("win")
#     elif block_num <= 1 and check_flag == 0:
#         check_flag = 2
#         print("draw")
#     return check_flag
#
# tic_map = make_map()
#
# print("x를 선택하려면 1, o를 선택하려면 2를 입력해 주세요: ")
# order = int(input())
# block_num = 9
# print("총 9개의 칸이 있습니다. 9개 칸 중 가장 왼쪽 위에 있는 칸은 0번, 가장 오른쪽 아래 있는 칸은 8번 입니다.")
# print(print_map(tic_map))
#
# while block_num > 0:
#
#     if order == 1:
#     # 플레이어 선, 컴퓨터 후
#         player_1 = int(input("x를 놓을 칸을 입력해 주세요: "))
#         if tic_map[player_1] == 0:
#             tic_map[player_1] = "x"
#             print("플레이어: {}".format(player_1))
#             block_num -= 1
#             computer = random.randrange(9)
#             while True:
#                 if tic_map[computer] == 0:
#                     tic_map[computer] = "o"
#                     print("컴퓨터: {}".format(computer))
#                     print(print_map(tic_map))
#                     block_num -= 1
#                     break
#                 else:
#                     computer = random.randrange(9)
#         else:
#             print("try again")
#
#         # 승부 확인
#
#     if order == 2:
#     # 컴퓨터 선, 플레이어 후
#         computer = random.randrange(9)
#         while True:
#             if tic_map[computer] == 0:
#                 tic_map[computer] = "o"
#                 print("컴퓨터: {}".format(computer))
#                 print(print_map(tic_map))
#                 block_num -= 1
#                 player_2 = int(input("o를 놓을 칸을 입력해 주세요: "))
#                 while True:
#                     if tic_map[player_2] != 0:
#                         player_2 = int(input("o를 놓을 칸을 입력해 주세요: "))
#                         depend = player_2
#                     else:
#                         tic_map[player_2] = "o"
#                         print("플레이어: {}".format(player_2))
#                         block_num -= 1
#                         print(print_map(tic_map))
#                         break
#             else:
#                 computer = random.randrange(9)
#
#
#         # 승부 확인
#
