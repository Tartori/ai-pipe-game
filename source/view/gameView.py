from model.gameModel import *
from pprint import pprint


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

    def printGameBoard(self, gameBoard: GameBoard, should_be_done):
        if not gameBoard.is_done and should_be_done:
            print("Could not solve board.")
            return
        print("Game Board:")
        print()
        self.__printBoarderLine(gameBoard)
        for line in gameBoard.gameBoardList:
            self.__printGameBoardTopValuesFromLine(line)
            self.__printGameBoardLeftRightValuesFromLine(line)
            self.__printGameBoardBottomValuesFromLine(line)
            self.__printBoarderLine(gameBoard)

    def __printBoarderLine(self, gameBoard: GameBoard):
        borderLine = "|"
        for _ in range(gameBoard.fieldsPerLine):
            borderLine += "---------|"
        print(borderLine)

    def __printGameBoardTopValuesFromLine(self,  line):
        # 2 times
        for _ in range(2):
            currentLine = "|"
            for field in line:
                if(field.isTopOpen == 1):
                    currentLine += "XXX i XXX"
                elif(field.isTopOpen == -1):
                    currentLine += "XXX o XXX"
                else:
                    currentLine += "XXXXXXXXX"
                currentLine += "|"
            print(currentLine)

    def __printGameBoardLeftRightValuesFromLine(self, line):
        currentLine = "|"
        for field in line:
            if(field.isLeftOpen == 1):
                currentLine += " i "
            elif(field.isLeftOpen == -1):
                currentLine += " o "
            else:
                currentLine += "XXX"
            currentLine += " w " if field.has_water() else "   "
            if(field.isRightOpen == 1):
                currentLine += " i "
            elif(field.isRightOpen == -1):
                currentLine += " o "
            else:
                currentLine += "XXX"
            currentLine += "|"
        print(currentLine)

    def __printGameBoardBottomValuesFromLine(self, line):
        # 2 times
        for _ in range(2):
            currentLine = "|"
            for field in line:
                if(field.isBottomOpen == 1):
                    currentLine += "XXX i XXX"
                elif(field.isBottomOpen == -1):
                    currentLine += "XXX o XXX"
                else:
                    currentLine += "XXXXXXXXX"
                currentLine += "|"
            print(currentLine)
            currentLine = ""
