from wonderwords import RandomWord
from wonderwords import RandomSentence
import sys
wrongGuesses = 0
guesses = []
def randomPhrase(): #Creates a Random Sentence using the Wonderwords library
    global phrase
    global WorP
    WorP = input('Would you like to play with a word (hard) of phrase (easy): ')
    if WorP.lower().rstrip() == 'phrase' or WorP.lower().rstrip() == 'easy':
        WorP = 'phrase'
        rs = RandomSentence()
        phrase = rs.sentence()
    elif WorP.lower().rstrip() == 'word' or WorP.lower().rstrip() == 'hard':
        WorP = 'word'
        rs = RandomWord()
        phrase = rs.word()
    else:
        print('Please input "word" or "phrase"')
        randomPhrase()
    return phrase

def generateSpaces(sentence): # Makes a list of underscores that is used as the displayed gameboard that gets filled with guesses
    global allSpaces
    global letters
    global wordsInSentence
    global allLetters
    allLetters = []
    sentenceNoPeriod = sentence.rstrip('.')
    wordsInSentence = sentenceNoPeriod.split()
    allSpaces = []

    for word in wordsInSentence:
        letters = list(word)
        spaces = []
        for n in range(len(letters)):
            allLetters.append(letters[n])
            spaces.append('_')
        for l in range(len(spaces)):
            allSpaces.append(spaces[l])

def printSpaces(): #Prints the gameboard
    x = 0
    for i in range(len(wordsInSentence)):
        for d in range(len(wordsInSentence[i])):
            print(allSpaces[x],end="")
            x += 1
        print(' ',end='')
    print('\n')

def inputLetter(): #takes the input and checs it is a single letter
    global guess
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha():
        print("Guess a letter.")
        inputLetter()
    elif len(guess) != 1:
        print('Guess 1 letter at a time.')
        inputLetter()
    elif guess in guesses:
        print('You inputed a letter you have already guessed, try again.')
        inputLetter() 
    guesses.append(guess)

def checkLetter(): # Checks if the letter is in the random sentence and adds it to the gameboard if so.
    global wrongGuesses
    global guesses
    isTrue = False
    inputLetter()
    for i in range(len(allLetters)):
        if guess == allLetters[i].lower() and i == 0:
            allSpaces[i] = guess.upper()
            isTrue = True
        elif guess == allLetters[i].lower():
            allSpaces[i] = guess
            isTrue = True
    if not isTrue:
        wrongGuesses += 1

def printStickman(wrongGuesses): # Prints the stickman depending on how many guesses the player had gotten wrong and ends the game when they have no more guesses.
    stickmanParts = [
        ["  _______ ", " |       |", " |", " |", " |", " |", "_|_"], #0 wrong guesses
        ["  _______ ", " |       |", " |       O", " |", " |", " |", "_|_"],  # 1 wrong guesses
        ["  _______ ", " |       |", " |       O", " |       |", " |", " |", "_|_"],  # 2 wrong guess
        ["  _______ ", " |       |", " |       O", " |      /|", " |", " |", "_|_"],  # 3 wrong guesses
        ["  _______ ", " |       |", " |       O", " |      /|\\", " |", " |", "_|_"],  # 4 wrong guesses
        ["  _______ ", " |       |", " |       O", " |      /|\\", " |      /", " |", "_|_"],  # 5 wrong guesses
        ["  _______ ", " |       |", " |       O", " |      /|\\", " |      / \\", " |", "_|_"]   # 6 wrong guesses
    ]

    if wrongGuesses < 6:
        print('\n'.join(stickmanParts[wrongGuesses]))
    else:
        print('\n'.join(stickmanParts[wrongGuesses]))
        print('The', WorP, 'was:', phrase)
        print("you lost")
        sys.exit()
        
def hasWon(): #checks if the player has won yet
    win = True
    for i in allSpaces:
        if i == '_':
            win = False
    if win:
        return True
#GameLoop
generateSpaces(randomPhrase())
while not hasWon():
    printStickman(wrongGuesses)
    printSpaces()
    checkLetter()
print('\n')
printSpaces()
print('You won!')
print('\n')
printSpaces()
print('You won!')
