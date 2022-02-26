import random



#File = open("Word_list.txt")
#lines = File.readlines() 

#Random_Word = random. randint(1,2317)
random_word = "plonk"


def guess_parser(guess_string, random_word):
    return_string = "*****"
    str = guess_string
    for index, letter in enumerate(str): 
        if letter in random_word and str[index] == random_word[index]:
            return_string = return_string[:index] + letter + return_string[index+1:]
        elif letter in random_word:
            print("The letter "+ letter + " shows up in the mystery word, but you placed it incorrectly.")
    return return_string

print(guess_parser("poium", random_word))


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
    guess = input("Guess:")
    guessparser(guess)