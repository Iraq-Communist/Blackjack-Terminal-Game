# Wordle-Terminal-Game
Portfolio Project for "Introduction to Programming 101" Course on Codecademy. 

Brainstorm : 
	* A .txt file containing the same word bank as the original NYT Wordle Game
	* multiple functions
	* first function initialises the game, welcomes the player, and picks a word at random from the word bank, which is on a differnet file. It saves it to a variable.  
	* Main Menu with 3 different options, "Play the game", which runs the main guessing game function, "See your statistics" which tracks amount of bad guesses, games won, games lost, etc. 
	* Main Guessing Game function continuously on a "while loop" with some logic implemented so that they can only guess 6 times. 
	* After each guess there should be a function ran within the main guessing game that uses string method logic to identify key letters, and to see if they are in the same index as the chosen mystery word; if it identifies the key letters but the indexes between the guess and the word don't match, it should tell the user that the letter they guessed was right, but not in the correct place.