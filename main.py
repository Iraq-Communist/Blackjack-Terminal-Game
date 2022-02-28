import random


with open("Word_list.txt","r") as File: 
    lines = File.readlines()



def guess_parser(guess_string, random_word):
    return_string = "*****"
    str = guess_string
    for index, letter in enumerate(str): 
        if letter in random_word and str[index] == random_word[index]:
            return_string = return_string[:index] + letter + return_string[index+1:]
        elif letter in random_word:
            print("The letter "+ letter + " shows up in the mystery word, but you placed it incorrectly.")
    return return_string


def main_menu():
    print("*"*90)
    print("Hello and welcome to the Terminal Wordle Game!\n")
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
    print("Guess the 5 letter word")
    print("*****")
    guess = input("Guess: " + "\n")
    if len(guess) == 5 and guess in lines:
        guess_parser(guess, random_word)
    else:
        print("Please input a 6 letter word that is a part of the word list.")
 
def statistics():
    pass

while 1==1:
    main_menu()
    userRes = getUserRes()
    if userRes == "1":
        random_word = random.choice(lines)
        gamefunc(random_word)

    elif userRes == "2":
        statistics()
    elif userRes == "3":
        print("Goodbye")
        exit()