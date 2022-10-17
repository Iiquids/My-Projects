import time
from Words import getRandomWord

'''
This project is gonna beat Edin's clapped up project
by Brayan and Edin
12 October 2022
'''

# all the crazy variables
totalTries = 0

''' This is just for debug and checking if I accidentally add duplicate words
for x in possibleWordList:
    if possibleWordList.count(x) != 1:
        print(possibleWordList[x]) '''

theWord = getRandomWord()
emptyBoxes = '[ ][ ][ ][ ][ ]'
answerBoard = []
fullAnswerBoard = []
avaliableKeyboard = ''' Q W E R T Y U I O P
  A S D F G H J K L
   Z X C V B N M''' # something Edin never worked on

#the color codes to spice things up
def prGreen(msg): return f"\033[1;32m{msg.upper()}\033[0m"
def prBlack(msg): return f"\033[0;30m{msg.upper()}\033[0m"
def prYellow(msg): return f"\u001b[33m{msg.upper()}\033[0m"
def prPurple(msg): return f"\033[0;35m{msg.upper()}\033[0m"

# now we gotta do the functions Edin told me to do
def wordChecker(wordInput):
    global avaliableKeyboard
    totalRow = ''
    for x in range(0, 5):
        if wordInput[x] == theWord[x]:
            greenLetter = prGreen(wordInput[x])
            totalRow = totalRow + f'[{greenLetter}]'
            avaliableKeyboard = avaliableKeyboard.replace(wordInput[x], greenLetter)
        elif wordInput[x] in theWord:
            totalRow = dupeChecker(wordInput[x], totalRow)
        else:
            blackLetter = prBlack(wordInput[x])
            totalRow = totalRow + f'[{blackLetter}]'
            avaliableKeyboard = avaliableKeyboard.replace(wordInput[x], blackLetter)
    winCheck(totalRow)
    fillBoard(totalRow)

def dupeChecker(letter, rowIP): # Edin doesn't have a repeat function so obviously my wordle is better
    global avaliableKeyboard
    dupeCount = theWord.count(letter)
    if dupeCount == 1:
        yellowLetter = prYellow(letter)
        totalRow = rowIP + f'[{yellowLetter}]'
        avaliableKeyboard = avaliableKeyboard.replace(letter, yellowLetter)
    else:
        purpleLetter = prPurple(letter)
        totalRow = rowIP + f'[{purpleLetter}]'
        avaliableKeyboard = avaliableKeyboard.replace(letter, purpleLetter)
    return totalRow

def fillBoard(currentRow):
    answerBoard.append(currentRow)
    for a in range(0, len(answerBoard)):
        fullAnswerBoard.append(answerBoard[a])
    for b in range(5 - totalTries):
        fullAnswerBoard.append(emptyBoxes)

def createAnswer():
    answer = ''
    for x in range(0, 5):
        greenLetter = prGreen(theWord[x])
        answer = answer + f'[{greenLetter}]'
    return answer

def winCheck(row): # Edin isn't gonna win so I don't have to worry about this function ever being used
    if createAnswer() in row:
        print('\nCONGRATS YOU BEAT betterWORDLE. THIS PROJECT IS BETTER THAN EDIN\'S!')
        fillBoard(row)
        for num in range(len(fullAnswerBoard)):
            print(fullAnswerBoard[num])
        time.sleep(1)
        exit()

def vowelNumCheck(wordInput):
    vowels = "AEIOU"
    vowelState = False
    for y in vowels:
        if y in wordInput:
            vowelState = True
    if len(wordInput) != 5:
        vowelState = False
    return vowelState
    
def alphaCheck(inWord):
    alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    verifier = 0
    for alphLetter in alph:
        for guessLetter in inWord:
            if alphLetter == guessLetter:
                verifier += 1
    if verifier == 5:
        return True
    else:
        return False

def guess(guessWord):
    guessWord = guessWord.upper()
    while vowelNumCheck(guessWord) == False:
        guessWord = input('Your word isn\'t a real world, Enter again: ')
        guessWord = guessWord.upper()
        vowelNumCheck(guessWord)
    while alphaCheck(guessWord) == False:
        guessWord = input('Your word isn\'t a real world, Enter again: ')
        guessWord = guessWord.upper()
        alphaCheck(guessWord)
    wordChecker(guessWord)
    for num in range(len(fullAnswerBoard)):
        print(fullAnswerBoard[num]) 
    print(f'  Avaliable letters: \n{avaliableKeyboard} \n')

# now for the tries loop
print('WELCOME TO betterWORDLE, THIS IS THE COMPETITION AGAINST EDIN\'S PROJECT\n') # welcome message
while totalTries != 6:
    fullAnswerBoard = []
    if totalTries == 0:
        guess(input('Enter your first 5 letter word: '))
    elif totalTries == 5:
        guess(input('This is your last guess, choose wisely: '))
        print(f'The Word: {theWord}')
    else:
        guess(input('Enter your next guess: '))
    totalTries += 1
