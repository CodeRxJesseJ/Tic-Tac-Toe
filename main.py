from functions import *

game_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
print(game_board[:3])
print(game_board[3:6])
print(game_board[6:])

update(game_board)
while game_won(game_board) == False:
    update(game_board)
    if game_won(game_board) == True:
        print("The game's over!")
        break
