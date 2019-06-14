# This is a "Choose your own adventure game"
import time

# Items, which provide specific benefits or extra options or certain scenarios
FLASHLIGHT = False
BACKROOM_KEYS = False
SECURITY_MONTIOR = False
BROOM_HANDLE = False
BANDAGES = False

# The intro to the game; sets the scene
def intro():
    print("You are locked in a dark hospital.")
    print("Strange noises echo from the surrounding hallway.")
    print("You don't know why you're here or where you came from, but you assume it would be best to get on the move.")
    print("Before you go, you see a table with a couple of objects, but a growing sense of urgency leads you to believe you only have time to grab one.")
    choice1()
    
# Gives the player a choice between three different items, and an option to pick none of them
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
        if firstChoice == '2':
            print("You grabbed the keys to the backroom.")
            BACKROOM_KEYS = True
        if firstChoice == '3':
            print("You grabbed the portable security monitor.")
            SECURITY_MONTIOR = True
        if firstChoice == '4':
            print("Despite your better judgement, you decide to move on without grabbing anything.")
        print("As you walk, you come across the entrance to a staircase, a branching hallway, and door to what seems to be a janitor's closet")
        choice2()
            
# Gives the player the choice between three paths, two leading to items, one leading to more options
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

# The one of the options for choice2(). Gives the player the broom handle if they have the flashlight and don't already have the broom handle
def choice2Closet():
    global BROOM_HANDLE
    print("The closet is dark and you can't make out what is in it.")
    if BROOM_HANDLE == True:
        print("You realize you have all you could get from the closet.")
    if FLASHLIGHT == True and BROOM_HANDLE == False:
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
            
# Another path of choice2(). Gives the player bandages if they have the backroom keys and don't already have the bandages
def choice2Hallway():
    global BANDAGES
    print("You make it through the hallway and it leads to a door.")
    print("It seems like a backroom of the hospital, it might contain supplies.")
    if BANDAGES == True:
        print("You remeber that you already have gotten all that you could from here, and turn back.")
        choice2()
    print("You try the handle.")
    time.sleep(1)
    print("It's locked.")
    if BACKROOM_KEYS == True:
        print("However, you happen to have the keys to the backroom.")
        print("You unlock the door and enter.")
        print("...It smells sterile.")
        print("You grab a roll of bandages. From the ominous sounds, you might need them.")
        BANDAGES = True 
    elif BACKROOM_KEYS == False:
        print("Without the keys, you're unable to do anything; this seems to be a dead end.")
    print("You head back to the crossroads.")
    choice2()

# The option of choice2() that continues the story, behind one door is an encounter with the monster, and behind the other is an escape. The player may also go back down stairs
def choice2Stairwell():
    print("You climb up the stairwell.")
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

# The pathway of choice2Stairwell() that leads to an escape, or death if the player chooses not to escape
def stairwellRight():
    print("You open the door to the right and...")
    print("You see a faint light at the end of the hallway.")
    print("As you approach, you see that the light is coming from the moon shining through a window.")
    print("The window leads to the outside. It's an escape!")
    print("You notice that, although the window is on the second floor, you could maybe survive the fall.")
    print("Do you jump out the window?")
    print("1 - Jump")
    print("2 - Don't jump")
    jumpOutWindow = ' '
    while jumpOutWindow != '1' or jumpOutWindow != '2':
        jumpOutWindow = input()
        if jumpOutWindow == '1':
            escape()
        if jumpOutWindow == '2':
            beastFindsYou()

# The encounter with the monster from choice2Stairwell(). The player may run from or fight the monster
def stairwellLeft():
    print("You open the door to your left and...")
    time.sleep(2)
    print("A fleshy monster leaps out from the shadows!")
    print("Will you run or fight?")
    print("1 - Run")
    print("2 - Fight")
    runOrFight = ' '
    while runOrFight != '1' or runOrFight != '2':
        runOrFight = input()
        if runOrFight == '1':
            runFromMonster()
        if runOrFight == '2':
            fightMonster()

# Second option of stairwellLeft(). Allows the player to fight the monster. If the broom handle item is obtained, the player lives. If not, they die
def fightMonster():
    global BROOM_HANDLE
    print("The beast lunges at you!")
    if BROOM_HANDLE == True:
        time.sleep(1)
        print("You barely manage to fend off the monstrosity with the broken broom handle you got from the closet.")
        print("After you ward it off, you slam the door, buying you some time before.")
        print("Unfortunately, your broom handle was torn into splinters in the process.")
        BROOM_HANDLE = False
        print("You're lucky to be alive, and you know you need to get out of here as quickly as possible.")
        print("You dash to the door to the right at the top of the stairwell.")
        time.sleep(3)
        stairwellRight()
    else:
        print("With nothing to ward off this monster, it swipes at your chest viciously.")
        print("You died.")
        finish()
        
# First option of stairwellLeft(). Allows the player to run from the monster. If the player does not have the bandages item, they will die
def runFromMonster():
    global BANDAGES
    print("You turn and sprint away from the beast.")
    print("It makes a quick, vicious swipe at you.")
    print("The swipe grazes you, causing immense pain.")
    print("You manage to escape, though, and you slam the door on the monster, buying you some time.")
    print("Your wound isn't fatal, but you need to stop the bleeding.")
    if BANDAGES == True:
        print("You quickly apply the bandages you got from the backroom.")
        print("You're lucky to be alive, and you know you need to get out of here as quickly as possible.")
        print("You dash to the door to the right at the top of the stairwell.")
        time.sleep(3)
        stairwellRight()
    else:
        time.sleep(2)
        print("You don't have anything to prevent you from bleeding out.")
        print("You pass out from blood loss...")
        print("You die shortly after.")
        finish()

# Choice of stairwellRight() where the player decides not to escape. Kills the player with no way to defend or escape
def beastFindsYou():
    print("Before you have time to find another escape, you turn and see a fleshy monster barreling toward you.")
    print("Caught off guard, you are killed near instantly as it crashes into you full-force.")
    print("You died.")
    finish()
    
# Choice of stairwellRight() where the player escapes and wins the game
def escape():
    print("You decide to take the risk and jump out the window.")
    time.sleep(1)
    print("You hit the ground in a tumble.")
    print("You think you may have broken a rib, or possibly fractured something in your leg, but at least you survived.")
    print("You escaped!")
    finish()

# Function that ends the "function rabbit hole" and prompts the game loop
def finish():
    playAgain = ' '
    while playAgain != 'yes' and playAgain != 'no':
        playAgain = input("Would you like to play agian?(yes or no) ")
        if playAgain == 'yes':
            FLASHLIGHT = False
            BACKROOM_KEYS = False
            SECURITY_MONTIOR = False
            BROOM_HANDLE = False
            BANDAGES = False
            intro()
        if playAgain == 'no':
            break

intro()

        
        


