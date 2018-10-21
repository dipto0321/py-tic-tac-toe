from pyfiglet import figlet_format
from classes.usefull import *


class Game:
    def __init__(self):
        self.box_list = []
        for i in range(1, 10):
            self.box_list.append(i)
        self.__combination = ("036", "147", "258", "012",
                              "345", "678", "048", "246")
        self.stop = False

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
        box_choose = input(
            "{} insert box number from above game board > ".format(player_obj.name))
        if not "1" <= box_choose <= "9" and self.box_list[int(box_choose)-1] is box_choose:
            print(
                "\nInvalid input.Please check gameboard avaiable number and input again\n")
            self.game_move(player_obj)
        player_obj.choices.append(int(box_choose) - 1)
        self.update_box_list(int(box_choose) - 1, player_obj.sign)
        player_obj.step += 1
        self.stop = self.game_state_check(player_obj)
        self.draw_board()

    def game_state_check(self, player_obj):
        choose_str = ''.join(map(str, player_obj.choices))
        choose_length = len(choose_str)
        if choose_length >= 3:
            move_choices = probability_comb(choose_str, 3)
            for move in move_choices:
                for won_comb in self.__combination:
                    if move == won_comb:
                        print("{} WON! in {} moves".format(
                            player_obj.name, player_obj.step))
                        return True

        if choose_length >= 4:
            return False

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

    def show_player_info(self):
        print("{} choose {} sign".format(self.name, self.sign))
