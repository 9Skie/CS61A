# The goal is to write a little battleships game, where both player picks the number to place their ship on.
# Then they guess where each other's ships are at, the player who guesses correctly first wins the game


player_1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

player_2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

player_round_count = 1
player_input_count = 0
p1_guess = ""
p2_guess = ""


def select_spot(x_cord, y_cord):
        if player_round_count == 1:
            special_position = player_1[x_cord][y_cord]
            return special_position
        elif player_round_count == 2:
            special_position = player_2[x_cord][y_cord]
            return special_position


print("Welcome to battleships! In this game, both players will pick a position to put their ship on in the 3x3 square,")
print("then when the game starts, both players will attempt to guess where the other player placed their ship!")
print("The first player who guesses correctly wins the game!")

while player_input_count < 2:
    try:

        if player_round_count == 1:
            print("\nThis is Player 1's choice of position!")
            X = int(input("Please input the X value of the desired position: "))
            Y = int(input("Please input the Y value of the desired position: "))
            p1_position = select_spot(X, Y)
            print("The spot picked is " + str(p1_position) + "!")

            player_round_count += 1
            player_input_count += 1
            
        elif player_round_count == 2:
            print("\nThis is Player 2's choice of position!")
            X = int(input("Please input the X value of the desired position: "))
            Y = int(input("Please input the Y value of the desired position: "))
            p2_position = select_spot(X, Y)
            print("The spot picked is " + str(p2_position) + "!")

            player_round_count -= 1
            player_input_count += 1
            
    except ValueError:
        print("That's not what the game asks for! All x and y coordinates should not anything else than numbers!")
    except IndexError:
        print("That's not what the game asks for! All x and y coordinates should be between 0 and 2 as a whole number!")


while p1_guess != p2_position and p2_guess != p1_position:
    try:

        if player_round_count == 1:
            print("\nIt's P1's turn!")
            X = int(input("Please input the X value of the desired guess position: "))
            Y = int(input("Please input the Y value of the desired guess position: "))
            p1_guess = player_2[X][Y]
            player_round_count += 1

            if p1_guess == p2_position:
                print("Player 1 wins! The spot Player 2 picked was indeed " + str(p2_position)) + exit()
            else:
                print("The spot picked \"" + str(p1_guess) + "\" is incorrect! Try another one when it's your turn!")

        elif player_round_count == 2:
            print("\nIt's P2's turn!")
            X = int(input("Please input the X value of the desired guess position: "))
            Y = int(input("Please input the Y value of the desired guess position: "))
            p1_guess = player_2[X][Y]
            player_round_count -= 1

            if p1_guess == p2_position:
                print("Player 2 wins! The spot Player 1 picked was indeed " + str(p1_position)) + exit()
            else:
                print("The spot picked \"" + str(p2_guess) + "\" is incorrect! Try another one when it's your turn!")
                
    except ValueError:
        print("That's not what the game asks for! All x and y coordinates should not anything else than numbers!")
    except IndexError:
        print("That's not what the game asks for! All x and y coordinates should be between 0 and 2 as a whole number!")

