#!/usr/bin/env python3.7
from model.gameModel import *
from view.gameView import *
from exceptions.exceptions import *
from copy import deepcopy
from pprint import pprint


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
        self.__alreadyPrinted = False

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
        # print(self.__gameModel.gameBoard.gameBoardList)

    def __isStringValueYesOrNo(self, inputString):
        if(inputString == "y" or inputString == "yes" or inputString == "no"):
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
        self.__gameView.printGameBoard(
            self.__gameModel.gameBoard, self.__alreadyPrinted)
        self.__alreadyPrinted = True

    def solve(self):
        self.__reached_states = []
        self.__gameModel.__gameBoard = self.solve_recursively(
            [self.__gameModel.gameBoard])

    def solve_recursively(self, moves, ):
        """
        for pawn in game.get_movable_pawns():
            for move in game.get_moves_for_pawn(pawn):
                movegame = deepcopy(game)
                movegame.do_move(pawn, move)
                movegame.to_next_turn()
                if movegame.get_winner() is not None:
                    return 100, pawn, move
                (opp, _, _) = self.__find_best_solution_rec(
                    depth-1, movegame, alpha)
                sol = -opp
                if(sol < alpha):
                    break
                alphamove = move
                alphapawn = pawn
                alpha = sol
        """
        board = moves.pop()
        moves.append(board)
        self.__reached_states.append(board)
        while not board.is_done() and len(moves) > 0:
            board = moves.pop()
            for line in range(board.lines):
                for column in range(board.fieldsPerLine):
                    moveboard = deepcopy(board)
                    moveboard.turn_field(line, column)
                    if moveboard in self.__reached_states:
                        continue
                    self.__reached_states.append(moveboard)
                    moves.append(moveboard)
        self.__gameView.printGameBoard(board, True)
