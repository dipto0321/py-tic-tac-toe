from pyfiglet import figlet_format
from .usefull import *
from itertools import permutations as perm


class Game:
    def __init__(self):
        self.box_list = [i for i in range(1, 10)]
        self.__combination = [(0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 1, 2),
                              (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6)]

    @staticmethod
    def show_title():
        print(figlet_format('Tic - Tac - Toe', font='doom'))
        print('==========================================================================')
        print('* * * Created by Dipto Karmakar || Created Date 18th September 2018 * * *')
        print(
            '==========================================================================\n')

    def draw_board(self):
        box_len = len(self.box_list)
        print("\nGame Board\n")
        for i in range(0, box_len):
            print(self.box_list[i], end="")
            if (i + 1) % 3 == 0:
                print('\n---------')
            else:
                print(' | ', end="")

    def plyars_info_collect(self):
        print("\nPlayer One Info")
        player_one = input("Your name: ")
        player_one_sign = input(
            "Your Sign [Any character you want]: ")
        print("\nPlayer two Info")
        player_two = input("Your name : ")
        player_two_sign = input(
            "Your Sign [Any character you want]: ")
        if player_one == player_two or player_one_sign == player_two_sign:
            print(
                "\n[ Found same information about players.Please insert diffrent info. ]\n")
            self.plyars_info_collect()
        return {player_one: player_one_sign,
                player_two: player_two_sign}

    def update_box_list(self, select_box, sign):
        self.box_list[select_box] = sign

    def game_move(self, player_obj):
        box_choose = int(input(
            "{} insert box number from above game board > ".format(player_obj.name)))
        if box_choose in self.box_list:
            player_obj.choices.append(box_choose - 1)
            self.update_box_list(box_choose - 1, player_obj.sign)
            player_obj.step += 1
            self.game_state_check(player_obj)
            if player_obj.win:
                print("{}, Congrates! ".format(player_obj.name))
                self.game_end()
            else:
                self.draw_board()

        else:
            print(
                "\nInvalid input.Please check gameboard avaiable number and input again\n")
            self.game_move(player_obj)

    def game_state_check(self, player_obj):
        length = len(player_obj.choices)
        if length >= 3:
            choice_comb = perm(player_obj.choices, 3)
            for comb in self.__combination:
                if comb in choice_comb:
                    player_obj.win = True
                    break

    def game_start(self):
        self.draw_board()

    def game_end(self):
        print("Thanks for playing!")


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign
        self.choices = []
        self.step = 0
        self.win = False

    def show_player_info(self):
        print("{} choose {} sign".format(self.name, self.sign))
