#How do we define a board, like the space is empty,it has a black piece,or it has a white piece, that stuff? (10 by 10 board)

#How do we define a player's turn? How do they input (where do they input) on the screen to say where their next piece goes?

#How do we check the winning conditions of a player? Like, 5 in a row, column, or diagonal, how do we check that?

#The Computer Opponet... How am I going to define him? How does the computer thing have sensible logic?

#Are we doing this in the pygame moduel or what...? I'm not personally really into pygame anyways, but I guess it's a little better than using purely command line displays
#We can get a tutorial to get myself a little back on track (even though, I really don't care to work with pygame ever again in my entire life) on the jists of pygame, it's not that rewarding

#Just command line, gomoku, with computer opponent




def print_board(board):

    #print new line
    print()
    
    #print small space indent
    print("  ", end= "")

    # print out 1 2 3 4 5 6 7 8 9
    for j in range(10):
        print(f"{j} ", end= "")

    #print new line
    print()

    for i in range(10):

        # print out 1 2 3 4 5 6 7 8 9 vertically
        print(i, end= " ")

        #actually prints out the rows of the board 1 by 1
        for j in range(10):
            if board[i][j] == 0:
                print(". ", end= "")
            elif board[i][j] == 1:
                print("X ", end= "")
            elif board[i][j] == 2:
                print("O ", end= "")
        print()



def get_move(player, board):
    while True:
        try:
            coordinates = input(f"Please give inputs of your desired move (in format of x,y), Player {player}: ")
            if len(coordinates) != 3 or coordinates[0].isdigit() != True or coordinates[2].isdigit() != True or coordinates[1] != ",":
                raise ValueError
            
            row, column = coordinates.split(",")
            row, column = int(column), int(row)

            if board[row][column] != 0:
                raise ValueError
        except (ValueError):
            print(f"Invalid move, Player {player}. Please format your input correctly.\n")
        else:
            break
    return row, column



def check_win(player, board):

    #checking vertically to see if 5 consecutive pieces of a player is placed
    for i in range(10):
        for j in range(5):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player and board[i][j + 4] == player:
                return True

    #checking horizontally
    for i in range(5):
        for j in range(10):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player and board[i + 4][j] == player:
                return True

    #checking diagonally (right)
    for i in range(5):
        for j in range(5):
             if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j +2] == player and board[i + 3][j +3] == player and board[i + 4][j + 4] == player:
                return True

    #checking diagonally (left)
    for i in range(5):
        for j in range(4, 10):
             if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == player and board[i + 4][j - 4] == player:
                 return True



def play_game():
    board = [[0]*10 for i in range(10)]
    player = 1
    while True:
        print_board(board)
        row, col = get_move(player, board)
        board[row][col] = player
        if check_win(player, board) == True:
            print()
            print_board(board)
            print("Player " + str(player) + " wins!")
            break
        player = 3 - player


if __name__ == "__main__":
    play_game()
