# Name: boardGamev3.py
# Authors: Eva Ho, Christian De La Hoz, Kemar Thomas, Ty Winkler
# Description: A game where the player is shown Python themed questions and advances
# across a virtual board
#
# Input: Player name, main menu selection and answers to cards
#
# Processing: 1. Declare and initialize variables
#                Menu choice, board position, decision to finish reading rules
#                (finishedRules) and to continue playing (playAgain)
#                Define menu and rule functions
#                Display program introduction message
#
#
#              2. Prompt for user name in introduction
#                   Display menu
#
#              3. If the user chooses to see the rules, display them and ask user if they are
#                   finished reading them
#                   If user chooses game, display each question and advance or retreat based
#                   on user input.
#                   If at the end of the game, the player has moved 20 or more spaces:
#                   Display congratulations
#                   If not, display consolation
#                 Prompt user to play again
#                 If user declines or chooses exit from the menu, terminate
#
#
#
#
# Output: Board position after each question answered correctly or incorrectly
#
from graphics import *
def main():

    # Declare and initialize variables

    intro = choice = ""
    playAgain = finishedRules = "yes"
    position = 0
    invalid = True
    fileName = "card.txt"
    # Define menu

    def displayMenu():
        print('\n1. See Rules')
        print('2. Play Game')
        print('3. Exit\n')

    # Define rules

    def showRule():
        print('\n\nHello, programmer! The FBI needs your assistance to catch a hacker.')
        print('10 Python questions will be shown in cards randomly.')
        print('If you give the right answer, you can move forward; otherwise, move backward.')
        print('\nYou will win the game after you have moved forward 20 steps.\n\n')

    # Introduction and greeting window

    intro = "\nWelcome to the FBI programmer game!\n"
    introWin = GraphWin("FBI Programmer", 720, 400)
    ruleButton = Rectangle(Point(100, 250), Point(200, 300))
    playButton = Rectangle(Point(300, 250), Point(400, 300))
    exitButton = Rectangle(Point(500, 250), Point(600, 300))
    #background = Image(Point(0,0), "fbi.gif")
    #background.draw(introWin)
    ruleButton.draw(introWin)
    playButton.draw(introWin)
    exitButton.draw(introWin)
    # Prompt user for their name

    name = input("Please enter your name: ")
    print("\nHello,", name)
    print("Let's start!")


    while playAgain == "yes":# This is our loop after checking for user input

        while invalid:
            try:
                displayMenu()
                choice = int(input("What would you like to do? (1/2/3): "))
                assert 1<=choice<=3
                invalid = False
            except ValueError:
                print("\nNot a valid choice. Please try again.\n")
            except AssertionError:
                print("\nPlease enter a number between 1 ~ 3.\n")


        try:
            if choice == 1:
                showRule()

                # Prompt to see if they're finished reading the rules

                finishedRules = input("Have you finished reviewing the rules?(yes/no): ").lower()
                if finishedRules == "yes":
                    invalid = True

                else:
                    continue

            # Start game. All answers are inputted as strings

            # Display position after each answer

            elif choice == 2:
                #opens the file contains cards
                fileName = "cards.txt"
                answer = ""
                position = 0
                fileExist = True
                qList = []
                pList = []
                aList = []
                try:
                    #open the card file
                    cards = open(fileName, "r").readlines()
                    for line in cards:
                        #seperate question, points, and answer in each line and store them in different lists
                        card = line.split("/")
                        qList.append(card[0])
                        pList.append(card[1])
                        aList.append(card[2])

                    for x in range(len(qList)):
                        answer = input(qList[x])
                        try:
                            answer = answer.lower()
                        except:
                            pass
                        #print(aList[x].strip())
                        if answer == aList[x].strip():
                            position += int(pList[x])
                            print("\nAdvance " ,pList[x], "steps!")
                        else:
                            print("You typed: ", answer, "\nCorrect answer:", aList[x])
                            position -= int(pList[x])
                            print("Retreat ", pList[x], " steps.")
                        print("You are currently at position ", position,"\n")

                    #Display results
                    if position >= 20:
                        print("Position: ", position)
                        print("\nCongratulations, ", name, "! You won!")

                    else:
                        print("Position: ", position)
                        print("\nI'm sorry, ", name,", you didn't quite make it.")
                        print("Better luck next time!")

                    position = 0
                    playAgain = input("\nAre you finished? Would you like to play again, yes or no? ")
                except:
                    print("File: {} does not exist. \nThe game can't continue without the file.".format(fileName))
                    print("Program is shutting down...... See you when you get the right file. Bye!")

                ###########################################################################

            elif choice == 3:
                print("Goodbye! See you next time~")
                playAgain = "no"

        except:
            print("Something went wrong. The game will restart.")
            main()

    # Solutation

    print("Thanks for playing!")

main()
