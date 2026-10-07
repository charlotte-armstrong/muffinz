import random

##defining main function
def main():
    options = [1,2,3]

    playerchoice = int(input('''Choose one: \n
    1. Rock
    2. Paper
    3. Scissors

    Enter THE CORRESPONDING NUMBER for your choice: '''))

    botchoice = random.choice(options)

    if playerchoice == botchoice:
        if playerchoice == 1:
            print("\nTie! Your rocks smashed each other to bits...\n")
        elif playerchoice == 2:
            print("\nTwo papers tried to fight and both failed to leave a dent on the other.\n")
        elif playerchoice == 3:
            print("\nYou both chose scissors? Seems like there's some chemistry going on... 🤨😏✂️✂️\n")
    elif playerchoice == 1 and botchoice == 2:
        print("\nThe bot chose paper and you chose rock.You got beat by a lame paper. Loser.\n")
    elif playerchoice == 1 and botchoice == 3:
        print("\nYou crushed the bot's scissors to bits with your massive boulder. Good job buddy.\n")
    elif playerchoice == 2 and botchoice == 1:
        print("\nSomehow your flimsy paper beat a rock. Great work I guess...?\n")
    elif playerchoice == 2 and botchoice == 3:
        print("\nThe bot sliced your paper to bits with its digital scissors. Better luck next time.")
    elif playerchoice == 3 and botchoice == 1:
        print("\nThe bot totally mangled your cheap kid scissors with its massive silicon CPU boulder. Shameful.\n")
    elif playerchoice == 3 and botchoice == 2:
        print("\nYou cut a piece of paper. Good job.\n")
    else:
        print("\nInvalid input. Restart the game, stupid.\n")


##main loop thingy
if __name__ == "__main__":
    main()