# This is a "Choose your own adventure game"
import time
# Items, which provide specific benefits or extra options or certain scenarios
FLASHLIGHT = False
BACKROOM_KEYS = False
SECURITY_MONTIOR = False
BROOM_HANDLE = False
# The intro to the game; sets the scene
def intro():
    print("You are locked in a dark hospital.")
    print("Strange noises echo from surrounding hallways.")
    print("You don't know why you're here or where you came from, but you assume it would be best to get on the move.")
    print("Before you go, you see a table with a couple of objects, but a growing sense of urgency leads you to believe you only have time to grab one.")
    
# Gives the player a choice between three different items
def choice1():
    global FLASHLIGHT, BACKROOM_KEYS, SECURITY_MONTIOR
    print("(Choose a starting item)")
    print("1 - Flashlight")
    print("2 - Backroom Keys")
    print("3 - Security Monitor")
    print("4 - None (not advised)")
    firstChoice = ' '
    while firstChoice != '1' or firstChoice !='2' or firstChoice != '3' or firstChoice != '4':
        firstChoice = input()
        if firstChoice == '1':
            print("You grabbed the flashlight.")
            FLASHLIGHT = True 
            break
        if firstChoice == '2':
            print("You grabbed the keys to the backroom.")
            BACKROOM_KEYS = True
            break
        if firstChoice == '3':
            print("You grabbed the portable security monitor.")
            SECURITY_MONTIOR = True
            break
        if firstChoice == '4':
            print("Despite your better judgement, you decide to move on without grabbing anything.")
            break

def choice2():
    print("Where do you go?")
    print("1 - Stairwell")
    print("2 - Hallway")
    print("3 - Closet")
    secondChoice = ' '
    while secondChoice != '1' or secondChoice !='2' or secondChoice != '3':
        secondChoice = input()
        if secondChoice == '1':
            choice2Stairwell()
        if secondChoice == '2':
            choice2Hallway()
        if secondChoice == '3':
            choice2Closet()

def choice2Closet():
    global BROOM_HANDLE
    print("The closet is dark and you can't make out what is in it.")
    if FLASHLIGHT == True:
        print("Luckily, you have a flashlight.")
        print("You turn it on and see...")
        time.sleep(1)
        print("Nothing much. You grab a broken broom handle because you have a feeling it might be useful later.")
        BROOM_HANDLE = True 
    print("You leave the closet.")
    print("You're back at the crossroads.")
    print("1 - Stairwell")
    print("2 - Hallway")
    secondChoice = ' '
    while secondChoice != '1' or secondChoice !='2':
        secondChoice = input()
        if secondChoice == '1':
            choice2Stairwell()
        if secondChoice == '2':
            choice2Hallway()

def choice2Stairwell():
    print("You climb up the stairwell", end = " ")
    if SECURITY_MONTIOR == True:
        print("You remeber the portable security monitor you grabbed and check this floor for danger.")
        print("Through the security feed, you see a silhouette of a monster ravaging through the room that's to your left.")
    print("There are two doors at the top of the stairwell, which do you enter?")
    print("1 - Enter the door to your left")
    print("2 - Enter the door to your right")
    print("3 - Go back down the stairs")
    leftOrRight = ' '
    while leftOrRight != '1' or leftOrRight !='2' or leftOrRight != '3':
        leftOrRight = input()
        if leftOrRight == '1':
            stairwellLeft()
        if leftOrRight == '2':
            stairwellRight()
        if leftOrRight == '3':
            choice2()
        
    
intro()
choice1()
print("As you walk, you come across the entrance to a staircase, a branching hallway, and door to what seems to be a janitor's closet")
choice2()

