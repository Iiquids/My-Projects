import random

possibleWords = ["Abuse", "Adult", "Agent", "Anger", "Apple", "Award", "Basis", "Beach", "Birth", "Block", "Blood", "Board", "Brain", "Bread", "Break", "Brown", "Buyer", "Cause", "Chain", "Chair", "Chest", "Chief", "Child", "China", "Claim", "Class", "Clock", "Coach", "Coast", "Court", "Cover", "Cream", "Crime", "Cross", "Crowd", "Crown", "Cycle", "Dance", "Death", "Depth", "Doubt", "Draft", "Drama", "Dream", "Dress", "Drink", "Drive", "Earth", "Enemy", "Entry", "Error", "Event", "Faith", "Fault", "Field", "Fight", "Final", "Floor", "Focus", "Force", "Frame", "Frank", "Front", "Fruit", "Glass", "Grant", "Grass", "Green", "Group", "Guide", "Heart", "Henry", "Horse", "Hotel", "House", "Image", "Index", "Input", "Issue", "Japan", "Jones", "Judge", "Knife", "Laura", "Layer", "Level", "Lewis", "Light", "Limit", "Lunch", "Major", "March", "Match", "Metal", "Model", "Money", "Month", "Motor", "Mouth", "Music", "Night", "Noise", "North", "Novel", "Nurse", "Offer", "Order", "Other", "Owner", "Panel", "Paper", "Party", "Peace" ]

## Variables
WORD = random.choice(possibleWords)
table = []
Empty = "【 】【 】【 】【 】【 】"
Answers = []

for i in WORD:
    table.append(i)
## Variable End

## Spooky Functions

def checkEqual(a, b):
    a = a.lower()
    b = b.lower()
    if a == b:
        return True
    else:
        return False

def turnGreen(msg):
    return f"\033[1;32m{msg.upper()}\033[0m"

def turnYellow(msg):
    return f"\u001b[33m{msg.upper()}\033[0m"

def turnBlack(msg):
    return f"\033[0;30m{msg.upper()}\033[0m"

def turnRed(msg):
    return f"\033[0;31m{msg}\033[0m"

def getStringColor(a):
    for i in range(0, len(WORD)):
        bool = checkEqual(a, table[i])
        if bool == True:
            return turnYellow(a)
    return turnBlack(a)

gameRounds = 0
def checkWord(text):
    global gameRounds
    final = ""
    guessTable = []
    Finished = 0
    for i in text:
        guessTable.append(i)

    for i in range(0, len(WORD)):
        bool = checkEqual(guessTable[i], table[i])
        stringColor = getStringColor(guessTable[i])
        if bool == True:
            Finished = Finished + 1
            local = guessTable[i]
            final = final + f"【{turnGreen(local)}】"
        else:
            final = final + f"【{stringColor}】"
    if Finished == 5:
        print(turnGreen("YOU GUESSSED IT! WINNER WINNER CHICKEN DINNER!"))
        exit()
    gameRounds = gameRounds + 1
    return final

def guess():
    global gameRounds
    guess = input()
    if len(guess) != 5:
        while len(guess) != 5:
            print(f"The Length Of {guess} is not 5.")
            guess = input()
    guess = guess.lower()
    round = checkWord(guess)
    Answers.append(round)
    for i in Answers:
        print(i)
    for i in range(0, 6-gameRounds):
        print(Empty)

#End Of Spooky Functions

print("Enter Your First Guess:")
guess()
print("Enter Your Secound Guess:")
guess()
print("Enter Your Third Guess:")
guess()
print("Enter Your Fourth Guess:")
guess()
print("Enter Your Fifth Guess:")
guess()
print("Enter Your Sixth Guess:")
guess()
print(turnRed("Welp... Out of Luck."))
