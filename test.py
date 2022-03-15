random_word = "Adieu"

def guess_parser(guess_string, random_word):
    return_string = "*****"
    for index, letter in enumerate(guess_string): 
        if letter in random_word and guess_string[index] == random_word[index]:
            return_string = return_string[:index] + letter + return_string[index+1:]
        elif letter in random_word:
            print("The letter "+ letter + " shows up in the mystery word, but you placed it incorrectly.")         
    return return_string
    

print(guess_parser("Arise", random_word))