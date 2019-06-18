#!/usr/bin/env python3.7

import random
from enum import Enum
from copy import deepcopy


class GameField:
    __isTopOpen: int
    @property
    def isTopOpen(self):
        return self.__isTopOpen

    __isRightOpen: int
    @property
    def isRightOpen(self):
        return self.__isRightOpen

    __isBottomOpen: int
    @property
    def isBottomOpen(self):
        return self.__isBottomOpen

    __isLeftOpen: int
    @property
    def isLeftOpen(self):
        return self.__isLeftOpen

    def has_entry_and_exit(self):
        return ((self.__isTopOpen == -1 or self.__isBottomOpen == -1 or self.__isRightOpen == -1 or self.__isLeftOpen == -1)) and (self.__isTopOpen == 1 or self.__isBottomOpen == 1 or self.__isRightOpen == 1 or self.__isLeftOpen == 1)

    def __init__(self, isTopOpen: int, isRightOpen: int, isBottomOpen: int, isLeftOpen: int):
        self.__isTopOpen = isTopOpen
        self.__isRightOpen = isRightOpen
        self.__isBottomOpen = isBottomOpen
        self.__isLeftOpen = isLeftOpen

    def turnField(self):
        return self.rightTurn()

    def rightTurn(self):
        return GameField(self.__isRightOpen, self.__isBottomOpen, self.__isLeftOpen, self.__isTopOpen)

    def __repr__(self):
        return f'GameField({self.__isTopOpen},{self.__isRightOpen},{self.__isBottomOpen},{self.__isLeftOpen})'


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
        for _ in range(gameBoardLines):
            line = []
            for _ in range(fieldsPerLine):
                line.append(None)
            self.__gameBoardList.append(line)

    def setInitialGameBoardState(self):
        self.__resetGameBoardState()

    def turn_field(self, line, column):
        self.__gameBoardList[line][column] = self.__gameBoardList[line][column].turnField(
        )

    def __resetGameBoardState(self):
        for lineIndex, line in enumerate(self.__gameBoardList):
            for fieldIndex, _ in enumerate(line):
                self.__gameBoardList[lineIndex][fieldIndex] = self.__getRandomGameField(
                )

    def __getRandomGameField(self):
        gameField = None
        while(gameField is None or not gameField.has_entry_and_exit()):
            gameField = GameField(self.__getRandomState(), self.__getRandomState(
            ), self.__getRandomState(), self.__getRandomState())
        return gameField

    def __getRandomState(self):
        r = 4
        while(r > 2):
            r = random.getrandbits(2)
        return r-1


class Direction(Enum):
    In = 1
    Out = -1
    Closed = 0


class GameModel:
    DEFAULT_FIELDS_PER_LINE = 3

    __gameBoard: GameBoard
    @property
    def gameBoard(self):
        return self.__gameBoard

    def createGameBoard(self, fieldsPerLine):
        self.__gameBoard = GameBoard(fieldsPerLine)
