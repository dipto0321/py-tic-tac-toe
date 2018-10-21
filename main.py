from classes.game import *
# TODO:
# FIXME: Box input same detection

new_game = Game()
new_game.show_title()
players_info = new_game.plyars_info_collect()
players = []
print("_____________\n")
for player in players_info:
    players.append(Player(player, players_info[player]))
    players[len(players) - 1].show_player_info()
print("\nBest of luck {} and {}".format(players[0].name, players[1].name))

new_game.game_start()
for i in range(5):
    if i == 4 and not new_game.stop:
        new_game.game_move(players[0])
        break
    elif not new_game.stop:
        new_game.game_move(players[0])
    if i == 4 and not new_game.stop:
        new_game.game_move(players[1])
        break
    elif not new_game.stop:
        new_game.game_move(players[1])
new_game.game_end()
