from controller.gameController import *
from model.gameModel import *
from view.gameView import *
from exceptions.exceptions import *

import sys


class Main:
    @staticmethod
    def main(args):
        gameModel = GameModel()
        gameView = GameView()
        gameController = GameController(gameModel, gameView)

        gameController.createGameBoard()
        gameController.displayGameBoard()

        gameController.solve()


if __name__ == '__main__':
    Main.main(sys.argv)
