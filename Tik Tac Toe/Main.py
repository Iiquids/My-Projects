import os, random

'''
SCUFFED TIC TAC TOE REMAKE ON PYTHON
by Brayan, Edin
started 14 October 2022

os.system('CLS') THIS CLEARS TERMINAL, INCASE FORGET HOW TO CLEAR
'''
# Variables
tikTable = [3, 3, 3, 3, 3, 3, 3, 3, 3]
somoneWon = False 
winningCombination = [ ## All Winning Combos!
    [ 0, 1, 2 ],
    [ 3, 4, 5 ],
    [ 6, 7, 8 ],
    [ 0, 3, 6 ],
    [ 1, 4, 7 ],
    [ 2, 5, 8 ],
    [ 0, 4, 8 ],
    [ 2, 4, 6 ],
]
availiabledigits = {"x" : [], "y": []}

# & C:/Users/alexi/AppData/Local/Microsoft/WindowsApps/python3.9.exe "c:/Users/alexi/OneDrive/Documents/Coding/Random py Scripts/TiktakToe.py"

cordnateHistory = [] # Usefull for Reaping Cordnates

def validNumberCheck(number): # checks to see if input is valid (only 1 or 2 allowed)
    while (number not in '12') or (len(number) == 1) == False:
        number = input('Enter only 1 or 2, try again: ')
    return number

def appendToTable(num, table):
    table.append(num)

def validCheck(number): # Checks If The Number is a 2 Digit, In The Alphabet, Amount is 0 or 1 or or 2
    global gamemode
    if (len(number) == 2) is False:
        print("Message Was Larger Then 2 Digits")
        return False
    for i in range(0, 2):
        if number[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxz!@#$%^&*()': # !
            print("Message Isnt A Number")
            return False
        ranges = 0
        if number[i] in '012' == False:
            ranges = ranges + 1
        if ranges >= 3:
            print("Number is Larger then 2")
            return False
    for i in cordnateHistory:
        if i == number:
            if gamemode == 2:
                print("Message Already Used")
                return False
            else:
                return False
    return True


def checkTableNumberv2(number): # Simply a function for the function Above
    while validCheck(number) == False:
        number = input("Invalid Number, try again: ")
        validCheck(number)
    appendToTable(number, cordnateHistory)
    return int(number[0]), int(number[1])

def checkIfEqualsEachother(a, b, c): # Checks if the 3 numbers are the same
    if a == b:
        if a == c:
            return a
    return False

def winCheck(): # Function Name Explains
    global somoneWon
    global tikTable
    for i in winningCombination:
        if checkIfEqualsEachother(tikTable[i[0]], tikTable[i[1]], tikTable[i[2]]) == 1:
            print("Player 1 Won!")
            somoneWon = True
        elif checkIfEqualsEachother(tikTable[i[0]], tikTable[i[1]], tikTable[i[2]]) == 2:
            if gamemode == 2:
                print("Player 2 Won!")
                somoneWon = True
                return
            else:
                print("Bot Wins!")
                somoneWon = True
                return

def drawCheck(): # Function Name Explains
    global somoneWon
    global tikTable
    answered = 0
    for i in tikTable:
        if i != 3:
            answered = answered + 1
    if answered == 9:
        if somoneWon != True:
            print("Draw!")
        somoneWon = True
    return

def pTable(): # Turns A the Tik Tac Toe Array Into a Table
    global tikTable
    global player
    newString = ''
    xyTable = []
    for i in tikTable:
        if i == 3:
            xyTable.append(" ")
        elif i == 2:
            xyTable.append("O")
        else:
            xyTable.append("X")

    newTable = ["     0   1   2\n", f"0    {xyTable[0]} | {xyTable[1]} | {xyTable[2]} ", "    ---+---+---" , f"1    {xyTable[3]} | {xyTable[4]} | {xyTable[5]} ", "    ---+---+---" ,f"2    {xyTable[6]} | {xyTable[7]} | {xyTable[8]} "]
    for i in newTable:
        newString = newString + i + "\n"
    return newString

def checkSimilarNumbersInTable(table1, table2): # Name Explains
    for x in table1:
        for y in table2:
            if x == y:
                return x
    
def getPosition(x, y): #Gets Position Of Number In TTT Table
    global tikTable
    xTable0 = [0, 3, 6]
    xTable1 = [1, 4, 7]
    xTable2 = [2, 5 ,8]
    yTable0 = [0, 1, 2]
    yTable1 = [3, 4, 5]
    yTable2 = [6, 7, 8]
    posX = ''
    posY = ''
    if x == 0:
        posX = xTable0
    elif x == 1:
        posX = xTable1
    elif x == 2:
        posX = xTable2
        
    if y == 0:
        posY = yTable0
    elif y == 1:
        posY = yTable1
    elif y == 2:
        posY = yTable2
    return posX, posY

##  blank{x} | x | O
##
##


def makeTable(x, y, player): # Makes a Array Based On The Player's Input
    global tikTable
    posX, posY = getPosition(x, y)
    similarNumber = checkSimilarNumbersInTable(posX, posY)
    tikTable[similarNumber] = player
    print(pTable())
    winCheck()
    drawCheck()

print('\tWelcome to tic-tac-toe but python and scuffed!\n')
gamemode = validNumberCheck(input('''Play with a bot: 1 \nPlay with a friend: 2\n'''))

if gamemode == '1': # Player VS Bot
    os.system('CLS')
    player = 1
    inputSpot = (input('''Player, Enter your X: \n
         0   1   2

    0      |   |   
        ---+---+---
    1      |   |   
        ---+---+---
    2      |   |   \n'''))
    digit1, digit2 = checkTableNumberv2(inputSpot)
    os.system('CLS')
    makeTable(digit1, digit2, player)
    while somoneWon == False: ## Keeps Looping Till Somone Won or It's A Draw
        player = 2
        botChoiceX = random.randint(0,2)
        botChoiceY = random.randint(0,2)
        botChoiceXY = str(botChoiceX) + str(botChoiceY)
        while validCheck(botChoiceXY) == False:
            print(f'messed up {botChoiceXY}')
            botChoiceX = random.randint(0,2)
            botChoiceY = random.randint(0,2)
            botChoiceXY = str(botChoiceX) + str(botChoiceY)
            print(botChoiceXY)
            validCheck(botChoiceXY)
        appendToTable(botChoiceXY, cordnateHistory)
        os.system('CLS')
        makeTable(botChoiceX, botChoiceY, player)
        if somoneWon == True:
            exit() ## Just Incase Player 2 Won Or Draw
        player = 1
        inputSpot = input('Player, Enter your X: ')
        digit1, digit2 = checkTableNumberv2(inputSpot)
        os.system('CLS')
        makeTable(digit1, digit2, player)
else: # Player VS Player
    os.system('CLS')
    player = 1
    inputSpot = (input('''Player One, Enter your X: \n
         0   1   2

    0      |   |   
        ---+---+---
    1      |   |   
        ---+---+---
    2      |   |   \n'''))
    digit1, digit2 = checkTableNumberv2(inputSpot)
    os.system('CLS')
    makeTable(digit1, digit2, player)
    while somoneWon == False: ## Keeps Looping Till Somone Won or It's A Draw
        player = 2
        inputSpot = input('Player Two, Enter your O: ')
        digit1, digit2 = checkTableNumberv2(inputSpot)
        os.system('CLS')
        makeTable(digit1, digit2, player)
        if somoneWon == True:
            exit() ## Just Incase Player 2 Won Or Draw
        player = 1
        inputSpot = input('Player One, Enter your X: ')
        digit1, digit2 = checkTableNumberv2(inputSpot)
        os.system('CLS')
        makeTable(digit1, digit2, player)
