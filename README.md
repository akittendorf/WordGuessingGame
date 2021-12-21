# WordGuessingGame
This is an exercise in creating a word guessing game.

Rules
A random word is chosen from a full dictionary list. A player starts with 7 guesses.
On each turn, a player can guess a letter or guess the full word. If the player guesses a letter that is in the word, the computer will show the player the position of each instance of that letter.

For example: Take the word "Mississippi" If the player chooses "i", the computer will print "_ i _ _ i _ _ i _ _ i " If the player then chooses, "o", the player will lose a 1 guess and now has 6 guesses.

When the player has 0 guesses, the game is over and the player has lost. If the player guesses the word correctly, the game is over and the player has won. If the player guesses the word incorrectly and the total guesses left is greater then 2, they lose 1 guess. If they guess the word incorrectly and the total guesses they have left is 1, they lose the game.

Part 1
Fully flowchart or pseudocode the game instructions. The input of the letter or word should be case insensitive and the pseudocode should include some logic to check user input to make sure it is either a letter or word.

Part 2
Pick a static word of your choice and code this into your solution. Utilizing the flowchart or pseudocode, demonstrate your understanding of the topics covered by utilizing functions, lists, dictionaries, sets, variables and string manipulation in your code.

Part 3
Replace the static word in Part 2 with a random word read in from a English word list file such as this English word list. You may use any file reader of your choice to read in and choose the word randomly. The game should run one time and then exit.

Part 4
After you have coded the initial game, change the game to ask the user if the player would like to play again. Keep a running total of wins and losses and ensure no word from Part 3 is ever picked twice for one session of the game.

Part 5
Devise a new way to use ASCII, f strings, and what we covered from the lessons to display how the player is doing on each turn.

Hint: You may read in or create as many additional files as you need to solve this problem.



