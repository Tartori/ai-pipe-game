from model.gameModel import *
from view.gameView import *
from exceptions.exceptions import *

class GameController:
    __gameModel: GameModel
    @property
    def gameModel(self):
        return self.__gameModel
    
    __gameView: GameView
    @property
    def gameView(self):
        return self.__gameView

    def __init__(self, gameModel: GameModel, gameView: GameView):
        self.__gameModel = gameModel
        self.__gameView = gameView
    
    def createGameBoard(self):
        fieldsPerLine = self.__gameModel.DEFAULT_FIELDS_PER_LINE
        while True:
            try:
                self.__gameView.printDefaultGameSizeQuestion()
                answer = input()
                if(not self.__isStringValueYesOrNo(answer)):
                    raise WrongAnswerToYesNoQuestion
                break
            except WrongAnswerToYesNoQuestion:
                self.__gameView.printWrongAnswerToYesNoQuestion()
        if(answer == "no"):
            fieldsPerLine = self.__getFieldsPerLineFromUserInput()
        
        #self.__gameModel.__gameBoard = GameBoard(fieldsPerLine)
        self.__gameModel.createGameBoard(fieldsPerLine)
        self.__gameModel.gameBoard.setInitialGameBoardState()
        #print(self.__gameModel.gameBoard.gameBoardList)

    def __isStringValueYesOrNo(self, inputString):
        if(inputString == "yes" or inputString == "no"):
            return True
        return False

    def __getFieldsPerLineFromUserInput(self):
        while True:
            try:
                self.__gameView.printEnterDesiredGameSizeQuestion()
                fieldsPerLine = int(input())
                if(not self.__isBetween3And6(fieldsPerLine)):
                    raise ValueNotBetweenThreeAndSix
                break
            except ValueError:
                self.__gameView.printNotANumberEntered()
            except ValueNotBetweenThreeAndSix:
                self.__gameView.printNotANumberBetweenThreeAndSixEntered()
        return fieldsPerLine

    def __isBetween3And6(self, number):
        if(number < 3 or number > 6):
            return False
        return True
    
    def displayGameBoard(self):
        self.__gameView.printGameBoard(self.__gameModel.gameBoard)