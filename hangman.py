# Hangman game


import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    # take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    string = ""
    x = 0
    for i in secretWord:
        if i not in lettersGuessed:
            string += ' _ '
        else:
            string += i
    return string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    string = []
    text= 'abcdefghijklmnopqrstuvwxyz'
    for i in text:
        if i not in lettersGuessed:
            string += i
    return string
    

def hangman(secretWord):
    guessedLetters = ''
    won = False
    guessesLeft = 8

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("__________________")

    while guessesLeft > 0:
        print(f'You have {guessesLeft} guesses left')
        availableLetters = getAvailableLetters(guessedLetters)
        print("Available letters:", ' '.join(availableLetters))
        
        guessedLettersThisTurn = ''
        while True:
            inputLetter = input("Please guess a letter: ").lower()

            if inputLetter in guessedLetters:
                print("Oops! You have guessed that letter already.")
            elif inputLetter not in availableLetters:
                print("Oops! You have guessed an invalid letter.")
            elif inputLetter in secretWord and inputLetter not in guessedLetters:
                guessedLetters += inputLetter
                print(f'Good Guess: {getGuessedWord(secretWord, guessedLetters)}')
                break
            else:
                guessedLettersThisTurn = inputLetter
                guessedLetters += inputLetter
                guessesLeft -= 1
                print(f'Oops!,That letter is not in my word: {getGuessedWord(secretWord, guessedLetters)}')
                break

        lettersCompleted = getGuessedWord(secretWord, guessedLetters)

        if isWordGuessed(secretWord, lettersCompleted):
            won = True
            break

    if won:
        print("Congratulations, you won!")
    else:
        print("Sorry, you lost the game. The answer was:", secretWord)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
