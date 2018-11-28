from classes.game import *
from random import randint


new_game = Game()
new_game.show_title()
players_info = new_game.plyars_info_collect()
players = []
print("_____________\n")
for player in players_info:
    players.append(Player(player, players_info[player]))
    players[len(players) - 1].show_player_info()
print("\nBest of luck {} and {}".format(players[0].name, players[1].name))
FIRST_MOVE = randint(0, 1)
SECOND_MOVE = 1 if FIRST_MOVE is 0 else 0

# new_game.game_start()
for i in range(4):
    new_game.game_move(players[FIRST_MOVE])
    new_game.game_move(players[SECOND_MOVE])
new_game.game_move(players[FIRST_MOVE])
# if not (players[0].win and players[1].win):
#     print('Match draw!\n')
new_game.game_end()
