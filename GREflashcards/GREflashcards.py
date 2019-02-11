
from graphics import *
from random import shuffle

def main():

    # Declare and initialize variables

    intro = name = choice = cardTitle = question = ""
    playAgain = finishedRules = "yes"
    position = count = 0
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


    # Introduction and greeting window

    intro = name + "\nLet's crash GRE verbal reasoning!\n"
    introWin = GraphWin("GRE voc", 720, 400)
    playButton = Rectangle(Point(300, 300), Point(400, 350))
    exitButton = Rectangle(Point(500, 300), Point(600, 350))
    playButtonText = Text(Point(350, 325), "Play")
    exitButtonText = Text(Point(550, 325), "Exit")
    greeting = Text(Point(350,250), intro)
    playButton.draw(introWin)
    exitButton.draw(introWin)
    playButtonText.draw(introWin)
    exitButtonText.draw(introWin)
    greeting.draw(introWin)

    mainScreen = True
    while mainScreen:
        buttonClick = introWin.getMouse()
        clickXPos = buttonClick.getX()
        clickYPos = buttonClick.getY()

        if 300 <= clickYPos <= 350:

            #when play is clicked
            if 300 <= clickXPos <= 400:
                position = 0
                fileExist = True
                qList = []
                pList = []
                aList = []

                try:

                    cards = open(fileName, "r").readlines()


                    for line in cards:
                        #seperate question, points, and answer in each line and store them in different lists

                        card = line.split("/")
                        print(card)
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
                        count += 1
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
                                text += "\n"+ str(count) +" / "+ str(len(cards))
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
