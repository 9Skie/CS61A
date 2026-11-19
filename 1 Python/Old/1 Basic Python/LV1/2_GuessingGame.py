answer = "九霄"
guess = ""
guess_times = 0
guess_limit = 3
out_of_guesses = False


def hints(index):
    if index == 0:
        print("The hint to the answer is... a character that shares some personalities of Jeff,")
        print("but has their own distinct traits and adventures that Jeff yearns to experience.\n")
        index2 = input("Please input your " + str(guess_times + 1) + "st guess: ")
        return index, index2
    elif index == 1:
        print("Additional hint! This character is from the game \"Houkai Gakuen 2\".")
        index2 = input("Please input your " + str(index + 1) + "nd guess: ")
        return index, index2
    elif index == 2:
        print("Last additional hint! This character name is referenced by Jeff in many of his online profiles.")
        index2 = input("Please input your " + str(index + 1) + "rd guess: ")
        return index, index2



print("Welcome to the guessing game! You have 3 chances to enter your guesses!")

while guess != answer and not out_of_guesses:
    if guess_times < guess_limit:
        (guess_times, guess) = hints(guess_times)
        if guess != answer:
            print("\nThat is wrong!")
        guess_times += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Chances used up! You lose! The answer is 九霄!")
    print("Guess you aren't that close to Jeff.")
else:
    print("\nThat is correct!")
    print("You certainly know a bit about Jeff.")
