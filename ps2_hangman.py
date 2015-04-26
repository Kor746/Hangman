# 6.00 Problem Set 2
# 
# Hangman
#
# Name          : Daniel Lee
# Collaborators : Me, Myself, and I
# Time spent    : 3 weeks

# -----------------------------------
# helper code
import random
import string
import time

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()


# your code begins here!
print ''
def hangman():
    ## The hangman game
    secretWord = choose_word(wordlist)
    guesses = 8
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is %d letters long' %len(secretWord)
    used_letters = []
    
    while True:
               
        print '-' * 30
        print "you have %d guesses left." %guesses
        print "Available letters: " + availableLetters(used_letters)

        request_word(secretWord, guesses)


        my_guess = request_letter()
        
        if my_guess not in used_letters:
            print 'Letters thats are used:'.upper(), letters(used_letters,my_guess)
        else:
            print 'Sorry, this letter has already been used'.upper(), letters(used_letters,my_guess)
            
        
        if my_guess in secretWord:
            print "Good guess:" + hidden_word(used_letters, secretWord)
        else:
            print "Oops! That letter is not in my word:" + hidden_word(used_letters, secretWord)
            guesses -= 1
            surrender(guesses,victory,used_letters,secretWord)
            if guesses == 0:
                print "The correct word was %s" %secretWord
                print "Game over"
                time.sleep(2)
                quit()
        
        if victory(used_letters, secretWord):
            time.sleep(2)
            print ""
            print "The correct word is %s" %secretWord
            print "Congratulations, you have won!"
            try_again = str(raw_input("Would you like to play again? ")).lower()
            if try_again == "yes":
                print "Okay, please wait"
                time.sleep(2)
                hangman()
            elif try_again == "no":
                print "Have a great day"
                break
        
            
########################################################################

## encapsulation begins here
        
def availableLetters(used_letters):
    ## Provides a new string of the alphabet everytime the letter is used
    new = ""
    for i in string.ascii_lowercase:
        if i not in used_letters:
            new += i
    return new
        
def hidden_word(used_letters, secretWord):
    ## Reveal hidden letter step by step
    new_word = ""
    for letter in secretWord:
       if letter in used_letters:
           new_word += letter
       elif len(secretWord) * '-':
           new_word += '-'
    return new_word
            
    

def request_word(secretWord, guesses):
    ## Ends game if you know the full word at any stage
    for i in range(0, guesses):
        my_word = str(raw_input("Do you know the word(yes/no)? ")).lower()
        if my_word == 'yes':
            final_word = str(raw_input("Enter the word: ")).lower()
            if final_word == secretWord:
                time.sleep(1.5)
                print 'Congratulations, you won!'
                print 'The word is %s' %secretWord
                retry = str(raw_input("Would you like to play again(yes/no)? ")).lower()
                if retry == 'yes':
                    time.sleep(1.5)
                    print '...'
                    time.sleep(1.5)
                    print '...'
                    time.sleep(1.5)
                    print 'Loading...'
                    time.sleep(1)
                    hangman()
                    
                elif retry == 'no':
                    print 'exiting module'
                    print '...'
                    time.sleep(1)
                    quit()
                    
            else:
                print 'This is not the correct word. Please try again!!!'
                continue
                    
        elif my_word == 'no':
            break
        
        
        
def letters(used_letters, my_guess):
    ## places letters that are used in a list
        if my_guess not in used_letters and len(my_guess) == 1:
           used_letters += my_guess
        return used_letters
        
def surrender(guesses,victory,used_letters,secretWord):
    ## Gives you option to surrender when you have lost a bit too many times
    for i in range(guesses):
        if victory(used_letters,secretWord):
            break
        else:
            if guesses < 6 and guesses % 2 != 0:
                give_up = str(raw_input('Would you like to give up(yes/no)? ')).lower()
                if give_up == 'yes':
                    print 'Exiting out of Hangman game...'
                    quit()

                elif give_up == 'no':
                    print 'Continuing...'
                    break
                               
def victory(used_letters, secretWord):
    ## Ends the game in victory once all letters are called
    
    for letter in secretWord:
        if letter not in used_letters:
            return False
    return True

def request_letter():
    letter = raw_input("Please guess a letter: ").lower()
    return letter

hangman()

##problems:
##1. Reduce guesses by 1 everytime the word is guessed incorrectly





    

