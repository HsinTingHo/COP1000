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
from random import shuffle

def main():

    # Declare and initialize variables

    intro = name = choice = cardTitle = question = ""
    playAgain = finishedRules = "yes"
    position = 0
    invalid = True
    fileName = "cards.txt"
    cardwidth = 500
    cardheigth = 300
    cardButtonRX = 200
    cardButtonLX = 300
    cardButtonUY = 200
    cardButtonDY = 250
    questionX = 250
    questionY = 150
    # Define menu

    #function for finding the middle point to place text
    def getMidPoint(p1, p2):
        return p1+(p2-p1)/2

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
    
    intro = name + "\nWelcome to the FBI programmer game!\n"
    introWin = GraphWin("FBI Programmer", 720, 400)
    ruleButton = Rectangle(Point(100, 300), Point(200, 350))
    playButton = Rectangle(Point(300, 300), Point(400, 350))
    exitButton = Rectangle(Point(500, 300), Point(600, 350))
    ruleButtonText = Text(Point(150, 325), "Show Rules")
    playButtonText = Text(Point(350, 325), "Play")
    exitButtonText = Text(Point(550, 325), "Exit")
    greeting = Text(Point(350,250), intro)
    background = Image(Point(360,100), "fbi.gif")
    background.draw(introWin)
    ruleButton.draw(introWin)
    playButton.draw(introWin)
    exitButton.draw(introWin)
    ruleButtonText.draw(introWin)
    playButtonText.draw(introWin)
    exitButtonText.draw(introWin)
    greeting.draw(introWin)

    mainScreen = True
    while mainScreen:
        buttonClick = introWin.getMouse()
        clickXPos = buttonClick.getX()
        clickYPos = buttonClick.getY()

        if 300 <= clickYPos <= 350:
            if 100 <= clickXPos <= 200:
                #rule window
                cardTitle = "Rules"
                msg = '\n\nHello, programmer! \nThe FBI needs your assistance to catch a hacker.\n'
                msg += '14 Python questions will be shown in cards randomly.\n'
                msg += 'If you give the right answer,\nyou can move forward; otherwise, move backward.\n'
                msg += '\nYou will win the game after you have moved forward 20 steps.\n\n'
                cardWin = GraphWin(cardTitle, cardwidth, cardheigth)
                rule = Text(Point(cardwidth/2, cardheigth/2), msg)
                rule.draw(cardWin)
            
            #when play is clicked
            if 300 <= clickXPos <= 400:
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

                    #shuffle a list of number between 0 and the size of the list
                    indexList = [index for index in range(len(qList))]
                    shuffle(indexList)
                    print(indexList)
                    
                    #loop through shuffled list to get random number of question
                    for x in indexList:
                        #make card
                        print(x)
                        cardTitle = "Question"
                        cardWin = GraphWin(cardTitle, cardwidth, cardheigth)

                        #swich line at 5th word to keep text in the window
                        
                        print(qList[x])
                        question = ""
                        word = qList[x].split(" ")
                        for i in range(len(word)):
                            
                            question += word[i] + " "
                            if i == 5:
                                question += "\n"
                            else:
                                continue
                                    

                        text = Text(Point(250, 100), question)
                        answerField = Entry(Point(cardwidth/2, 5+cardheigth/2), 10)
                        yesButton = Rectangle(Point(cardButtonLX, cardButtonUY), Point(cardButtonRX, cardButtonDY))
                        yesText = Text(Point(getMidPoint(cardButtonLX, cardButtonRX), getMidPoint(cardButtonUY, cardButtonDY)), "Submit")
                        text.draw(cardWin)
                        yesButton.draw(cardWin)
                        yesText.draw(cardWin)
                        answerField.draw(cardWin)

                        submit = True                            
                        while submit:
                            buttonClick = cardWin.getMouse()
                            clickXPos = buttonClick.getX()
                            clickYPos = buttonClick.getY()

                            if  200 <= clickXPos <= 300 and 200 <= clickYPos <= 250:
                                try:
                                    answer = answerField.getText().lower()
                                except:
                                    print("check answer input")

                                #Display result
                                cardTitle = "Result"
                                resultWin = GraphWin(cardTitle, cardwidth, cardheigth)
                                
                           
                                yesButton = Rectangle(Point(cardButtonLX, cardButtonUY), Point(cardButtonRX, cardButtonDY))
                                yesText = Text(Point(getMidPoint(cardButtonLX, cardButtonRX), getMidPoint(cardButtonUY, cardButtonDY)), "Next")
                                
                                if answer == aList[x].strip():
                                    position += int(pList[x])
                                    text = "Advance " +pList[x]+ " steps!"
                                else:
                                    position -= int(pList[x])
                                    text = "You typed: "+ answer+ "\nCorrect answer: "+ aList[x]
                                    text += "Retreat "+ pList[x]+ " steps."
                                    
                                text += "You are currently at position "+ str(position)+"\n"
                                msg = Text(Point(cardwidth/2, cardheigth/2), text)
                                msg.draw(resultWin)
                                yesButton.draw(resultWin)
                                yesText.draw(resultWin)

                                nextCard = True
                                while nextCard:
                                    buttonClick = resultWin.getMouse()
                                    clickXPos = buttonClick.getX()
                                    clickYPos = buttonClick.getY()
                                    if  200 <= clickXPos <= 300 and 200 <= clickYPos <= 250:
                                        resultWin.close()
                                        cardWin.close()
                                        break
                                break #break while submit
                       
                    #Display results
                    cardWin = GraphWin(cardTitle, cardwidth, cardheigth)
                    if position >= 20:
                        text = "Position: "+ str(position) +"\n"+ "\nCongratulations, "+ name+ "! You won!"
                        
                    else:
                        text = "Position: "+ str(position)+"\n"+"\nI'm sorry, "+ name+", you didn't quite make it."+"\nBetter luck next time!"
                    text += "\nAre you finished? Would you like to play again?"
                    yesButton =  Rectangle(Point(100, 250), Point(200, 280))
                    noButton = Rectangle(Point(300, 250), Point(400, 280))
                    yesText = Text(Point(150, 265), "Yes")
                    noText = Text(Point(350, 265), "No")
                    msg = Text(Point(cardwidth/2, cardheigth/2), text)
                    msg.draw(cardWin)
                    yesButton.draw(cardWin)
                    noButton.draw(cardWin)
                    yesText.draw(cardWin)
                    noText.draw(cardWin)

                    keepPlay = True
                    while keepPlay:
                        buttonClick = cardWin.getMouse()
                        clickXPos = buttonClick.getX()
                        clickYPos = buttonClick.getY()
                        if 250 <= clickYPos <= 280:
                            if 100 <= clickXPos <= 200:
                                print("yes!!!")
                                position = 0
                                keepPlay = False
                                cardWin.close()
                                break
                            if 300<= clickXPos <= 400:
                                print("no!!!")
                                keepPlay = False
                                cardWin.close()
                                mainScreen = False
                                introWin.close()
                    
                
                    
                    
                except  OSError:
                    print("File: {} does not exist. \nThe game can't continue without the file.".format(fileName))
                    print("Program is shutting down...... See you when you get the right file. Bye!")

            #when exit is clicked
            if 500 <= clickXPos <= 600:
                cardTitle = "Exit"
                msg = "Are you sure you want to quit?"
                cardWin = GraphWin(cardTitle, cardwidth, cardheigth)
                text = Text(Point(cardwidth/2, cardheigth/2), msg)
                yesButton = Rectangle(Point(cardButtonLX, cardButtonUY), Point(cardButtonRX, cardButtonDY))
                yesText = Text(Point(getMidPoint(cardButtonLX, cardButtonRX), getMidPoint(cardButtonUY, cardButtonDY)), "Yes")
                text.draw(cardWin)
                yesButton.draw(cardWin)
                yesText.draw(cardWin)

                stay = True
                while stay:
                    buttonClick = cardWin.getMouse()
                    clickXPos = buttonClick.getX()
                    clickYPos = buttonClick.getY()
                    if 200 <= clickXPos <= 300 and 200 <= clickYPos <= 250:
                        print("right here!")
                        stay = False
                        cardWin.close()
                        mainScreen = False
                        introWin.close()
                        


main()
