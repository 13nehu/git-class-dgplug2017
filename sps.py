import random

gamelist = ["stone", "paper", "scissor"]
print "Lets start the game choose any one option from STONE , PAPER , SCISSOR "

while True :
    choice = raw_input("Enter your choice :")
    syschoice = random.choice(gamelist)
    print "Other player choose" + syschoice
    if(syschoice == "stone"):
        if(choice == "paper"):
            print ":) yeah!! You win"
        elif(choice == "scissor"):
            print ":( You loose"
        else : 
            print "-_- Draw"
    if(syschoice == "paper"):
            if(choice == "scissor"):
                print ":) yeah!! You win"
            elif(choice == "stone"):
                print ":( You loose"
            else :
                    print "-_- Draw"

    if(syschoice == "scissor"):
            if(choice == "paper"):
                print ":) yeah!! You win"
            elif(choice == "stone"):
                print ":( You loose"
            else :
                    print "-_- Draw"
    y=raw_input("want to play again (yes to play again and no to quit) -")
    if(y=="NO" or y=="no"):
        break
