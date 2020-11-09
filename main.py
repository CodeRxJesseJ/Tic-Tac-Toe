from functions import *

game_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
print(game_board[:3])
print(game_board[3:6])
print(game_board[6:])

update(game_board)
while game_won(game_board) == False:
    update(game_board)
    if game_won(game_board) == True:
        if game_board.count("O") > game_board.count("X"):
            print("O has won the game!")
        else:
            print("X has won the game!")
    elif game_won(game_board) == False:
        if (game_board.count("X") == 5 and game_board.count("O") == 4) or (game_board.count("X") == 4 and game_board.count("O") == 5):
            print("Oh no! The game's a draw!")
            replay = input("Wanna play again? (Y/N): ")
            while replay != "Y" or "N":
                if replay == "Y":
                    print("Run the program agin then xD")
                    break
                elif replay == "N":
                    print("Take care, goodbye!")
                    break

print("NOTE: If you are getting an error, then maybe you might have not followed the rules properly!")
print("Please take time to visit https://en.wikipedia.org/wiki/Tic-tac-toe")
print("Thank you for playing!")
