import random


class GameField:
    __isTopOpen: bool
    @property
    def isTopOpen(self):
        return self.__isTopOpen

    __isRightOpen: bool
    @property
    def isRightOpen(self):
        return self.__isRightOpen

    __isBottomOpen: bool
    @property
    def isBottomOpen(self):
        return self.__isBottomOpen

    __isLeftOpen: bool
    @property
    def isLeftOpen(self):
        return self.__isLeftOpen

    def __init__(self, isTopOpen: bool, isRightOpen: bool, isBottomOpen: bool, isLeftOpen: bool):
        self.__isTopOpen = isTopOpen
        self.__isRightOpen = isRightOpen
        self.__isBottomOpen = isBottomOpen
        self.__isLeftOpen = isLeftOpen

    def turnField(self):
        self.rightTurn()

    def rightTurn(self):
        self.__isTopOpen, self.__isRightOpen, self.__isBottomOpen, self.__isLeftOpen = self.__isRightOpen, self.__isBottomOpen, self.__isLeftOpen, self.__isTopOpen


class GameBoard:
    __gameBoardList = []
    @property
    def gameBoardList(self):
        # convert list to tuple -> that only this class can change values
        # Code from: https://stackoverflow.com/questions/5506511/python-converting-list-of-lists-to-tuples-of-tuples
        list_of_lists = self.__gameBoardList
        tuple_of_tuples = tuple(tuple(x) for x in list_of_lists)
        return tuple_of_tuples

    __fieldsPerLine = 0
    @property
    def fieldsPerLine(self):
        return self.__fieldsPerLine

    __lines = 0
    @property
    def lines(self):
        return self.__lines

    __totalFields = 0
    @property
    def totalFields(self):
        return self.__totalFields

    def __init__(self, fieldsPerline):
        self.createEmpytyGameBoard(fieldsPerline)
        self.__lines = len(self.__gameBoardList)
        self.__fieldsPerLine = len(self.__gameBoardList[0])
        self.__totalFields = sum(len(field) for field in self.__gameBoardList)

    def createEmpytyGameBoard(self, fieldsPerLine):
        gameBoardLines = fieldsPerLine
        for i in range(gameBoardLines):
            line = []
            for i in range(fieldsPerLine):
                line.append(None)
            self.__gameBoardList.append(line)

    def setInitialGameBoardState(self):
        self.__resetGameBoardState()

    def __resetGameBoardState(self):
        threeSomeGameField = GameField(False, True, True, True)
        twoSomeField = GameField(False, False, True, True)
        forSomeField = GameField(True, True, True, True)

        for lineIndex, line in enumerate(self.__gameBoardList):
            for fieldIndex, field in enumerate(line):
                self.__gameBoardList[lineIndex][fieldIndex] = self.__getRandomGameField(
                )

    def __getRandomGameField(self):
        gameField = GameField(self.__getRandomBoolean(), self.__getRandomBoolean(
        ), self.__getRandomBoolean(), self.__getRandomBoolean())
        return gameField

    def __getRandomBoolean(self):
        return bool(random.getrandbits(1))


class GameModel:
    DEFAULT_FIELDS_PER_LINE = 3

    __gameBoard: GameBoard
    @property
    def gameBoard(self):
        return self.__gameBoard

    def createGameBoard(self, fieldsPerLine):
        self.__gameBoard = GameBoard(fieldsPerLine)
