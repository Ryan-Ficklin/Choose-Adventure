# This is a "Choose your own adventure game"
import time
# Items, which provide specific benefits or extra options or certain scenarios
flashlight = 0
backroomKeys = 0
securityMonitor = 0
# The intro to the game; sets the scene
def intro():
    print("You are locked in a dark hospital.")
    print("Strange noises echo from surrounding hallways.")
    print("You don't know why you're here or where you came from, but you assume it would be best to get on the move.")
    print("Before you go, you see a table with a couple of objects, but a growing sense of urgency leads you to believe you only have time to grab one.")
    
# Gives the player a choice between three different items
def choice1():
    global flashlight, backroomKeys, securityMonitor
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
            flashlight+=1
            break
        if firstChoice == '2':
            print("You grabbed the keys to the backroom.")
            backroomKeys += 1
            break
        if firstChoice == '3':
            print("You grabbed the portable security monitor.")
            securityMonitor += 1
            break
        if firstChoice == '4':
            print("Despite your better judgement, you decide to move on without grabbing anything.")
            break

def choice2():
    print("As you walk, you come across the entrance to a staircase, a branching hallway, and door to what seems to be a janitor's closet")
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
    print("The closet is dark and you can't make out what is in it.")
    if flashlight == 1:
        print("Luckily, you have a flashlight.")
        print("You turn it on and see...")
        time.sleep(1)
        print("Nothing much. You grab a broken broom handle because you have a feeling it might be useful later.")
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
intro()
choice1()
choice2()

