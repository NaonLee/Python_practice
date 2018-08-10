#Name: Naon Lee
#Date: May 30, 2018
#purpose: Code a Python program for simple guess game


import random   #The computer thinks of a number between 1 and 100

go = 'y'    
print("This is the simple guess game. Guess the number between 1 to 100.(You have 5 chances)\n")

while go == 'y' or go == 'Y' :              #If user type y, game will be continue
    print("--------------------------------------\n") 
    print("Game start!!")
    print("--------------------------------------\n")

    
    guess_number = random.randrange(1,100)          #For providing the number randomly
    chance = 5
    flag = True
    while flag == True :
        
        print("You have " + str(chance) + " chances/chance left.\n")        #Show the chance that user has
        guess = int(input("Please guess the number (only positive integer between 1 and 100): "))       #be typed number by user
        chance = chance -1              #Count the chance
        
        if guess_number == guess :              #If user give correct number
            print("\nThat is corret!\n")
            print("You won the game!!\n")
            flag = False                        #End the game(stop the while loop)
        
        else :
            if chance == 0 :                    #If user has no chance
                print("\n--------------------------------------\n")
                print("You lost the game, the number was " + str(guess_number) + "\n")
                flag = False                    #End game
            else :
                
                print("\nThat is wrong! please try agian!")
                
                if guess_number > guess :           #Give some hint to user
                    print("Hint! The number is higher than yours\n")
                else :
                    print("Hint! The number is lower than yours\n")
            

        
    print("--------------------------------------")
    print("Game End")
    print("--------------------------------------\n\n")
    
    go = input("Do you want to do it again? (if you want, type y or Y and do not want, type any key): ")    #user can select continue or quit the game

print("\n\nGoodbye!!")
