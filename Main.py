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

def printY(msg):
    print(f"\u001b[33m {msg}")

def printG(msg):
    print(f"\033[1;32m {msg}")

def getBrickColor(a):
    greyEmoji = "⬛"
    yellowEmoji = "🟨"
    for i in range(0, len(WORD)):
        bool = checkEqual(a, table[i])
        if bool == True:
            return yellowEmoji
    return greyEmoji

gameRounds = 0
def checkWord(text):
    global gameRounds
    greenEmoji = "🟩"
    final = ""
    guessTable = []
    Finished = 0
    for i in text:
        guessTable.append(i)

    for i in range(0, len(WORD)):
        bool = checkEqual(guessTable[i], table[i])
        brickColor = getBrickColor(guessTable[i])
        if bool == True:
            Finished = Finished + 1
            final = final + f"[{greenEmoji}]"
        else:
            final = final + f"[{brickColor}]"
    if Finished == 5:
        print("YOU GUESSSED IT! WINNER WINNER CHICKEN DINNER!")
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
""" _______________________
【   】【   】【   】【   】【   】
【   】【   】【   】【   】【   】
【   】【   】【   】【   】【   】
【   】【   】【   】【   】【   】
【   】【   】【   】【   】【   】
【   】【   】【   】【   】【   】
 ----------------------- """
 
 #Table
 
 #Change String Color

print("Enter Your Fifth Guess:")
guess()
print("Enter Your Sixth Guess:")
guess()
print("Welp... Out of Luck.")
