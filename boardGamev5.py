# Name: boardGamev5.py
# Authors: Eva Ho, Christian De La Hoz, Kemar Thomas, Ty Winkler
# Description: A game where the player is shown Python themed questions and advances
# across a virtual board
#
# Input: Player name,  and answers to cards
#Processing: 1. Display a window to take user name
#            2. Display greeting message, rule button, play button, and exit button on a window
#            4. If user clicks play button,
#              a. Pop out question window.
#                a-1. Display questions from card.txt file and take user input for the answer
#              b. Pop out a results
#                b-1. window to inform user whether the input was correct and the points gained(or lost)
#                b-2. On the same window,  display user's current point
#              c. When user finish answering all the questions, pop out window to ask whether user wants to play again
#                c-1 If user click yes, repeat step 4
#                c-2 If user click no, display confirmation window to confirm whether the user want to quit
#                  c-2.2 If user clicked no, close the confirm window
#            5. If user clicks exit button
#              5-1 Pop out a confirmation window to confirm whether the user want to quit
#              5-2 If user clicked yes, exit the programmer
#              5-3 If user clicked no, close the confirm window
#
#Output: name window, name input box, greeting window, rule window, question window, position window, question, answer input box, exit window


from graphics import *

def main():

    # Declare and initialize variables

    intro = name = choice = ""
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
        msg = '\n\nHello, programmer! The FBI needs your assistance to catch a hacker.'
        msg += '10 Python questions will be shown in cards randomly.'
        msg += 'If you give the right answer, you can move forward; otherwise, move backward.'
        msg += '\nYou will win the game after you have moved forward 20 steps.\n\n'
        ruleWin = GraphWin("Rules", 300, 200)
        rule = Text(Point(60, 70), msg)
        rule.draw(ruleWin)

    # Prompt user for their name
    nameWin = GraphWin("User Name", 500, 250)
    inputEntry = Entry(Point(350, 100), 10)
    inputEntry.setText("YourName")
    inputEntry.setFill("black")
    inputEntry.setTextColor("light green")
    inputLabel = Text(Point(175, 100), "Enter your name, please:")
    # Create Continue button
    firstButton = Rectangle(Point(200,140), Point(300, 175))
    firstButton.setFill("silver")
    firstButtonText = Text(Point(250, 155), "Continue")
    firstButton.draw(nameWin)
    firstButtonText.draw(nameWin)
    inputEntry.draw(nameWin)
    inputLabel.draw(nameWin)



    nameContinue = False
    while not nameContinue:
        buttonClick = nameWin.getMouse()
        name = inputEntry.getText()
        clickXPos = buttonClick.getX()
        clickYPos = buttonClick.getY()

        if 200 <= clickXPos <= 300 and 140 <= clickYPos <= 175:
            nameContinue = True
            displayText = Text(Point(250, 200), "Let's begin, " + name +"!")
            displayText.draw(nameWin)
            time.sleep(3)
            nameWin.close()
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









'''
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

                #finishedRules = input("Have you finished reviewing the rules?(yes/no): ").lower()
                #if finishedRules == "yes":
                    #invalid = True

                #else:
                    #continue

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
'''
main()
