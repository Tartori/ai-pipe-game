# --- Model ---
import math
class GameBoard:
    gameBoard = []

    def initializeGameBoard(self, fieldsPerLine):
        
        threeSomeGameField = GameField(False, True, True, True)
        twoSomeField = GameField(False, False, True, True)
        forSomeField = GameField(True, True, True, True)
        totalAmountOfFields = fieldsPerLine * fieldsPerLine
        '''
        GameBoard.gameBoard.append(threeSomeGameField)
        GameBoard.gameBoard.append(forSomeField)
        GameBoard.gameBoard.append(twoSomeField)
        GameBoard.gameBoard.append(threeSomeGameField)
        GameBoard.gameBoard.append(twoSomeField)
        GameBoard.gameBoard.append(threeSomeGameField)
        GameBoard.gameBoard.append(threeSomeGameField)
        GameBoard.gameBoard.append(twoSomeField)
        GameBoard.gameBoard.append(forSomeField)
        '''
        
        for i in range(0, totalAmountOfFields):
            if(i == 2):
                GameBoard.gameBoard.append(twoSomeField)
            elif(i == 9):
                GameBoard.gameBoard.append(forSomeField)
            else:
                GameBoard.gameBoard.append(threeSomeGameField)
    
    def isUneven(self, number):
        result = number % 2
        if(result == 0):
            return False
        return True

class GameField:

    def __init__(self, isTopOpen, isRightOpen, isBottomOpen, isLeftOpen):
        self.__isTopOpen = isTopOpen
        self.__isRightOpen = isRightOpen
        self.__isBottomOpen = isBottomOpen
        self.__isLeftOpen = isLeftOpen
    
    def getIsTopOpen(self):
        return self.__isTopOpen
    
    def getIsRightOpen(self):
        return self.__isRightOpen
    
    def getIsBottomOpen(self):
        return self.__isBottomOpen
    
    def getIsLeftOpen(self):
        return self.__isLeftOpen

    def rightTurn():
        print("Not yet implemented.")

    def leftTurn():
        print("Not yet implemented.")

# --- View ---
class GameBoardView:

    def printBoarderLine(self, fieldsPerLine):
        borderLine = "|"
        for x in range(0, fieldsPerLine):
            borderLine += "---------|"
        print(borderLine)

    def displayGameBoard(self, gameBoard: GameBoard):
        amountOfGameFields = len(gameBoard)
        amountOfLines = int(math.sqrt(amountOfGameFields))
        amountOfLineFields = amountOfLines
        lineCount = 0
        currentLine = ""

        self.printBoarderLine(amountOfLineFields)
        # foreach line
        for line in range(0, amountOfLines):
            # PRINT TOPLINE
            # 2 times
            for i in range(0, 2):
                currentLine = "|"
                # foreach field of line
                for lineField in range(0, amountOfLineFields):
                    if(gameBoard[lineField+(line*amountOfLineFields)].getIsTopOpen()):
                        currentGameFieldValue = "XXX   XXX"
                    else:
                        currentGameFieldValue = "XXXXXXXXX"
                    currentLine += currentGameFieldValue + "|"
                print(currentLine)
                currentLine = ""
            # PRINT TOPLINE

            # PRINT LEFTANDRIGHTLINE
            # foreach field of line
            currentLine = "|"
            for lineField in range(0, amountOfLineFields):
                if(gameBoard[lineField+(line*amountOfLineFields)].getIsLeftOpen()):
                    currentGameFieldValue = "   "
                else:
                    currentGameFieldValue = "XXX"
                currentLine += currentGameFieldValue + "   "
                if(gameBoard[lineField+(line*amountOfLineFields)].getIsRightOpen()):
                    currentGameFieldValue = "   "
                else:
                    currentGameFieldValue = "XXX"
                currentLine += currentGameFieldValue + "|"
            print(currentLine)
            # PRINT LEFTANDRIGHTLINE
            
            # PRINTBOTTOMLINE -> similar to TOPLINE
            # 2 times
            for i in range(0, 2):
                currentLine = "|"
                # foreach field of line
                for lineField in range(0, amountOfLineFields):
                    if(gameBoard[lineField+(line*amountOfLineFields)].getIsBottomOpen()):
                        currentGameFieldValue = "XXX   XXX"
                    else:
                        currentGameFieldValue = "XXXXXXXXX"
                    currentLine += currentGameFieldValue + "|"
                print(currentLine)
                currentLine = ""
            # PRINTBOTTOMLINE

            # PRINTBOARDERLINE
            self.printBoarderLine(amountOfLineFields)
            # PRINTBOARDERLINE

# --- Main ---
class Main:
    def printBoarderLine():
        print("|---------|---------|---------|")
    
    def printExampleOfGameFieldWithInputAndOutput(self):
        self.printBoarderLine()
        print("|XXX ^ XXX|XXX | XXX|XXXXXXXXX|")
        print("|XXX | XXX|XXX v XXX|XXXXXXXXX|")
        print("|-->   -->|-->   -->|-->   <--|")
        print("|XXX | XXX|XXXXXXXXX|XXX | XXX|")
        print("|XXX v XXX|XXXXXXXXX|XXX v XXX|")
        self.printBoarderLine()
        print("|XXX | XXX|XXX ^ XXX|XXX | XXX|")
        print("|XXX v XXX|XXX | XXX|XXX v XXX|")
        print("|XXX   <--|-->   -->|-->   -->|")
        print("|XXX ^ XXX|XXXXXXXXX|XXX | XXX|")
        print("|XXX | XXX|XXXXXXXXX|XXX v XXX|")
        self.printBoarderLine()
        print("|XXX ^ XXX|XXX ^ XXX|XXX | XXX|")
        print("|XXX | XXX|XXX | XXX|XXX v XXX|")
        print("|XXX   -->|XXX   -->|XXX   -->|")
        print("|XXXXXXXXX|XXX | XXX|XXX | XXX|")
        print("|XXXXXXXXX|XXX v XXX|XXX v XXX|")
        self.printBoarderLine()

    def printExampleOfGameField(self):
        self.printBoarderLine()
        print("|XXX   XXX|XXX   XXX|XXXXXXXXX|")
        print("|XXX   XXX|XXX   XXX|XXXXXXXXX|")
        print("|         |         |         |")
        print("|XXX   XXX|XXXXXXXXX|XXX   XXX|")
        print("|XXX   XXX|XXXXXXXXX|XXX   XXX|")
        self.printBoarderLine()
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX      |         |         |")
        print("|XXX   XXX|XXXXXXXXX|XXX   XXX|")
        print("|XXX   XXX|XXXXXXXXX|XXX   XXX|")
        self.printBoarderLine()
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX      |XXX      |XXX      |")
        print("|XXXXXXXXX|XXX   XXX|XXX   XXX|")
        print("|XXXXXXXXX|XXX   XXX|XXX   XXX|")
        self.printBoarderLine()
    
    def printSimpleExampleOnlyThreeSomeElements(self):
        self.printBoarderLine()
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|         |         |         |")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        self.printBoarderLine()
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|         |         |         |")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        self.printBoarderLine()
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|XXXXXXXXX|XXXXXXXXX|XXXXXXXXX|")
        print("|         |         |         |")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        print("|XXX   XXX|XXX   XXX|XXX   XXX|")
        self.printBoarderLine()

    @classmethod
    def main(self):
        print("--- EXAMPLES ---")
        print("Just print an example:")
        self.printExampleOfGameField(self)
        print("")
        print("Only threeSome elements:")
        self.printSimpleExampleOnlyThreeSomeElements(self)
        print("")
        print("Example with Inputs and Outputs")
        self.printExampleOfGameFieldWithInputAndOutput(self)
        print("--- EXAMPLES ---")
        print("")

        fieldsPerLine = 5
        gameBoard = GameBoard()
        gameBoardView = GameBoardView()
        gameBoard.gameBoard = gameBoard.initializeGameBoard(fieldsPerLine)
        print("Current GameBoard")
        gameBoardView.displayGameBoard(GameBoard.gameBoard)

Main.main()
