# 6

def update(game_board):
    pos = ""
    while pos not in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
        pos = input("Choose the position you want to play in [0 - 8]:")
    char = ""
    while char.upper() not in ["O", "X"]:
        char = input("Choose your item [ O / X ]: ")
    index = game_board.index(pos)
    game_board.remove(pos)
    game_board.insert(index, char)
    print(game_board[:3])
    print(game_board[3:6])
    print(game_board[6:])

# 8

def game_won(game_board):
    if (game_board[0] == game_board[4] == game_board[8]) or (
            game_board[2] == game_board[4] == game_board[6]
    ) or (game_board[1] == game_board[4] == game_board[7]) or (
            game_board[3] == game_board[4] == game_board[5]) or (
                game_board[0] == game_board[1] == game_board[2]) or (
                    game_board[6] == game_board[7] == game_board[8]) or (
                        game_board[3] == game_board[0] == game_board[6]) or (
                            game_board[2] == game_board[5] == game_board[8]):
        return True
    else:
        return False
