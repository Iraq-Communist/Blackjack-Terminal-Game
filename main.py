import random

with open("Word_list.txt","r") as File: 
    lines = File.read().splitlines()

games_won = 0
games_lost = 0
games_played = 0

def guess_parser(guess_string, random_word):
    return_string = "*****"
    for index, letter in enumerate(guess_string): 
        if letter in random_word and guess_string[index] == random_word[index]:
            return_string = return_string[:index] + letter + return_string[index+1:]
        elif letter in random_word:
            print("The letter "+ letter + " shows up in the mystery word, but you placed it incorrectly.")
            
    print(return_string)
    return

def main_menu():
    print("*"*90)
    print("Hello and welcome to the Terminal Wordle Game!")
    print("*"*90)
    print("Here are all the services we offer:\n")
    print("1) Play Wordle")
    print("2) View your game statistics")
    print("3) Exit Terminal Wordle Game")

def getUserRes():
    userRes = input("Your choice: ")
    if userRes == "1" or userRes == "2" or userRes == "3":
        return userRes
    else:
        print("Please only input 1, 2, or 3.")
        return getUserRes()

def gamefunc(random_word):
    global games_lost
    global games_won
    rounds_played = 0 
    game_won = False
    print("Guess the 5 letter word")
    print("*****")
    while game_won == False and rounds_played < 6:
            guess = input("Guess: ")
            if len(guess) == 5 and guess in lines:
                rounds_played += 1
                guess_parser(guess, random_word)
                print("Rounds played: " + str(rounds_played))
                if guess == random_word:
                    game_won = True
                    print("Wordle Complete!")
                    print("Congratulations on beating the Wordle!")
                    games_won += 1
            else:
                print("Please input a 5 letter word that is a part of the word list.")
    if game_won == False:
        print("Game over, try again by pressing 1 in main menu! The word was " + random_word + ".")
        games_lost += 1

def statistics():
    print("*"*90)
    print("Hello and welcome to the Statistics Section\n")
    print("*"*90)
    print("You have won " + str(games_won) + " games")
    print("You have lost " + str(games_lost) + " games")
    if games_played > 0:
        print("Your winrate is " + str(games_won / games_played * 100) + " %")

while True:
    main_menu()
    userRes = getUserRes()
    if userRes == "1":
        games_played += 1
        random_word = random.choice(lines)
        gamefunc(random_word)

    elif userRes == "2":
        statistics()
    elif userRes == "3":
        print("Goodbye")
        exit()