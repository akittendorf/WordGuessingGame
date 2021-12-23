# WORD GUESSING GAME
# get static word
# word = 'Beesly'
# import random and time modules
import random
import time
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
        time.sleep(1)
        # validate guess
        if guess.isalpha() == False:
            print("Hey, that's not a number! Try guessing a word or a letter.")
            time.sleep(1)
            continue
        # repeat guess
        if guess in correct_guessed or guess in incorrect_guessed:
            print('You already guessed this. Try something else.') 
            time.sleep(1)
            continue
        # correct guess
        elif guess == word:
            game_won = True
            break
        elif guess in word:
            print('Nice job! {} is in the word.'.format(guess))
            time.sleep(1)
            # update guessed list
            correct_guessed.append(guess)
            # print revealed letters
            current_word = [letter if letter in correct_guessed else '-' for letter in word]
            print(*current_word)
        # incorrect guess
        else:
            # add guess to incorrect_guessed
            incorrect_guessed.append(guess)
            # print incorrect message
            print('Sorry, {} is not in the word.'.format(guess))
            time.sleep(1)
            # update remaining_guesses
            remaining_guesses = remaining_guesses -1
    # player lost
    if game_won == False:
        print('Out of guesses :(')
        time.sleep(1)
        print('The word was {}. Better luck next time!'.format(word))
        time.sleep(1)
        # update score
        games_lost = games_lost + 1
    # player won
    else:
        print('Congratulations, you guessed the word! It was {}'.format(word))
        time.sleep(1)
        # update score
        games_won = games_won + 1
    # prompt user for another game
    answer = False
    while answer == False:
        play_again = input('Would you like to play again? Y/N')
        time.sleep(1)
        if play_again != 'Y' and play_again != 'N':
            print("Invalid format. Please enter 'Y' to play again or 'N' to end game.")
            time.sleep(1)
        elif play_again == 'Y':
            answer = True
            print('Great! Preparing your next word.')
            time.sleep(1)
            print('You have won {} game(s) and lost {} game(s)'.format(games_won,games_lost))
            time.sleep(1)
        else:
            answer = True
            print('Okay. Thanks for playing!')
            time.sleep(1)
            print('You won {} game(s) and lost {} game(s)'.format(games_won,games_lost))
            time.sleep(1)
            quit()
    
    
        
        
        