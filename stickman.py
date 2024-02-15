from wonderwords import RandomSentence
import sys
wrongGuesses = 0
guesses = []

def randomPhrase():
  rs = RandomSentence()
  return rs.sentence()


def generateSpaces(sentence):
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

def printSpaces():
    x = 0
    for i in range(len(wordsInSentence)):
        for d in range(len(wordsInSentence[i])):
            print(allSpaces[x],end="")
            x += 1
        print(' ',end='')
    print('\n')

def checkLetter():
    global wrongGuesses
    global guesses
    isTrue = False
    guess = input("Guess a letter: ").lower()
    if guess in guesses:
        print('You inputed a letter you have already guessed, try again.')
        checkLetter()
    guesses.append(guess)
    for i in range(len(allLetters)):
        if guess == allLetters[i].lower() and i == 0:
            allSpaces[i] = guess.upper()
            isTrue = True
        elif guess == allLetters[i].lower():
            allSpaces[i] = guess
            isTrue = True
    if not isTrue:
        wrongGuesses += 1

def printStickman(wrongGuesses):
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
        print("you lost")
        sys.exit()
        
def hasWon():
    win = True
    for i in allSpaces:
        if i == '_':
            win = False
    if win:
        return True
generateSpaces(randomPhrase())
while not hasWon():
    printStickman(wrongGuesses)
    printSpaces()
    checkLetter()
printSpaces()
print('You won!')
