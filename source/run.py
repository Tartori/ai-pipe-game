from controller.gameController import *
from model.gameModel import *
from view.gameView import *
from exceptions.exceptions import *

import sys


class Main:
    def main(args):
        gameModel = GameModel()
        gameView = GameView()
        gameController = GameController(gameModel, gameView)

        gameController.createGameBoard()
        gameController.displayGameBoard()

        gameController.solve()
        gameController.displayGameBoard()

    if __name__ == '__main__':
        main(sys.argv)
