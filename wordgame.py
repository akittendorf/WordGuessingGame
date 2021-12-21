# part 2 pseudocode
# choose static word, use lower()
# game won = False
# prompt user for guess while remaining guesses > 0
    # guess.lower() is in word       
        # guess == word
            # game won = True
            # break
        # guess != word
            # remaining guesses -1
            # continue
    # guess.lower() not in word
        # remaining guesses -1
# if game won == False
    # lose game
# if won game == True
    # win game
        
# WORD GUESSING GAME
# get static word
# word = 'Beesly'
# import random module
import random
# initialize play_game and score
play_game = True
games_won = 0
games_lost = 0
# load English words file
with open('words_alpha.txt') as words:
    words_list = words.read().split()
# start game loop
while play_game == True:
    # generate random number
    word_index = random.randrange(0,len(words_list))
    # get word, remove it from words_list, and convert to lowercase
    word = words_list.pop(word_index)
    # initialize game won, guess count, and lists of guessed
    game_won = False
    remaining_guesses = 7
    correct_guessed = []
    incorrect_guessed = []
    # prompt user for guess while remaining_guesses > 0
    while remaining_guesses > 0:
        guess = input('The word is {} letter(s) long. Guess a letter or the word itself. You have {} guess(es) remaining.'.format(len(word),remaining_guesses)).lower()
        # validate guess
        if guess.isalpha() == False:
            print("Hey, that's not a number! Try guessing a word or a letter.")
            continue
        # repeat guess
        if guess in correct_guessed or guess in incorrect_guessed:
            print('You already guessed this. Try something else.') 
            continue
        # correct guess
        elif guess == word:
            game_won = True
            break
        elif guess in word:
            print('Nice job! {} is in the word.'.format(guess))
            # update guessed list
            correct_guessed.append(guess)
            # print revealed letters
            current_word = [letter if letter in correct_guessed else '-' for letter in word]
            print(*current_word)
            # update remaining_guesses
            remaining_guesses = remaining_guesses - 1
        # incorrect guess
        else:
            # add guess to incorrect_guessed
            incorrect_guessed.append(guess)
            # print incorrect message
            print('Sorry, {} is not in the word.'.format(guess))
            # update remaining_guesses
            remaining_guesses = remaining_guesses -1
    # player lost
    if game_won == False:
        print('Out of guesses :(')
        print('The word was {}. Better luck next time!'.format(word))
        # update score
        games_lost = games_lost + 1
    # player won
    else:
        print('Congratulations, you guessed the word! It was {}'.format(word))
        # update score
        games_won = games_won + 1
    # prompt user for another game
    answer = False
    while answer == False:
        play_again = input('Would you like to play again? Y/N')
        if play_again != 'Y' or play_again != 'N':
            print("Invalid format. Please enter 'Y' to play again or 'N' to end game.")
        elif play_again == 'Y':
            answer = True
            print('Great! Preparing your next word.')
        else:
            answer = True
            print('Okay. Thanks for playing!')
            print('You won {} game(s) and lost {} game(s)'.format(games_won,games_lost))
            quit()
    
    
        
        
        