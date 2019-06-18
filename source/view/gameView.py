from model.gameModel import *


class GameView:
    def printDefaultGameSizeQuestion(self):
        print("Do you want to use the default Game Size? (yes or no):")

    def printWrongAnswerToYesNoQuestion(self):
        print("Answer has to be either yes or no. Try again.")

    def printEnterDesiredGameSizeQuestion(self):
        print(
            "Enter the desired fields per Line (has to be a number between 3 and 6:")

    def printNotANumberEntered(self):
        print("You did not enter a number. Try again.")

    def printNotANumberBetweenThreeAndSixEntered(self):
        print("You did not enter a number between 3 and 6. Try again.")

    def printGameBoard(self, gameBoard: GameBoard):
        print("Game Board:")
        print("")
        self.__printBoarderLine(gameBoard)
        for lineIndex, line in enumerate(gameBoard.gameBoardList):
            self.__printGameBoardTopValuesFromLine(gameBoard, line, lineIndex)
            self.__printGameBoardLeftRightValuesFromLine(
                gameBoard, line, lineIndex)
            self.__printGameBoardBottomValuesFromLine(
                gameBoard, line, lineIndex)
            self.__printBoarderLine(gameBoard)

    def __printBoarderLine(self, gameBoard: GameBoard):
        borderLine = "|"
        for x in range(0, gameBoard.fieldsPerLine):
            borderLine += "---------|"
        print(borderLine)

    def __printGameBoardTopValuesFromLine(self, gameBoard: GameBoard, line, lineIndex):
        # 2 times
        for i in range(0, 2):
            currentLine = "|"
            for fieldIndex, _ in enumerate(line):
                if(gameBoard.gameBoardList[lineIndex][fieldIndex].isTopOpen == 1):
                    currentGameFieldValue = "XXX i XXX"
                elif(gameBoard.gameBoardList[lineIndex][fieldIndex].isTopOpen == -1):
                    currentGameFieldValue = "XXX o XXX"
                else:
                    currentGameFieldValue = "XXXXXXXXX"
                currentLine += currentGameFieldValue + "|"
            print(currentLine)
            currentLine = ""

    def __printGameBoardLeftRightValuesFromLine(self, gameBoard: GameBoard, line, lineIndex):
        currentLine = "|"
        for fieldIndex, lineField in enumerate(line):
            if(gameBoard.gameBoardList[lineIndex][fieldIndex].isLeftOpen == 1):
                currentGameFieldValue = " i "
            elif(gameBoard.gameBoardList[lineIndex][fieldIndex].isLeftOpen == -1):
                currentGameFieldValue = " o "
            else:
                currentGameFieldValue = "XXX"
            currentLine += currentGameFieldValue + "   "
            if(gameBoard.gameBoardList[lineIndex][fieldIndex].isRightOpen == 1):
                currentGameFieldValue = " i "
            elif(gameBoard.gameBoardList[lineIndex][fieldIndex].isRightOpen == -1):
                currentGameFieldValue = " o "
            else:
                currenGameFieldValue = "XXX"
            currentLine += currentGameFieldValue + "|"
        print(currentLine)

    def __printGameBoardBottomValuesFromLine(self, gameBoard: GameBoard, line, lineIndex):
        # 2 times
        for i in range(0, 2):
            currentLine = "|"
            for fieldIndex, lineField in enumerate(line):
                if(gameBoard.gameBoardList[lineIndex][fieldIndex].isBottomOpen == 1):
                    currentGameFieldValue = "XXX i XXX"
                elif(gameBoard.gameBoardList[lineIndex][fieldIndex].isBottomOpen == -1):
                    currentGameFieldValue = "XXX o XXX"
                else:
                    currentGameFieldValue = "XXXXXXXXX"
                currentLine += currentGameFieldValue + "|"
            print(currentLine)
            currentLine = ""
