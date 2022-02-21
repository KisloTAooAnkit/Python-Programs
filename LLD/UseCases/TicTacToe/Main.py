
import uuid
from enum import Enum

class GameStatus(Enum):
    First,Second,Draw,Unfinished = 1,2,3,4

class Stats:
    def __init__(self) -> None:
        self.wins = 0
        self.loss = 0
    
    @property
    def getWinRate(self):
        if self.wins == 0 and self.loss == 0:
            return None
        return 100* self.wins / (self.wins + self.loss)

    def updateStats(self,flag):
        if flag:
            self.wins += 1
        else:
            self.loss += 1

class Move:
    def __init__(self,row,col,player) -> None:
        self.row = row
        self.col = col
        self.player = player

class User:
    def __init__(self,name) -> None:
        self.id = uuid.uuid4()
        self.stats = Stats()
        self.name = name


class Board:
    def __init__(self,player1,player2) -> None:
        self.board = [[0]*3 for _ in range(3)]
        self.rowC = [0]*3
        self.colC = [0]*3
        self.p1 = player1
        self.p2 = player2
        self.upperDiagC = 0
        self.loweDiagC = 0
        self.turn = True #True P1 , False P2
        self.gameStatus = GameStatus.Unfinished
        self.emptySlots = 9

    def printBoard(self):
        for i in self.board:
            print(i)
        print()
    
    def __checkWinner(self,i,j):
        if self.colC[j] == 3 or self.colC[j] == -3:
            return True
        if self.rowC[i] == 3 or self.rowC[i] == 3:
            return True
        if self.loweDiagC == 3 or self.loweDiagC == -3:
            return True
        if self.upperDiagC == 3 or self.upperDiagC == -3:
            return True
        
        return False

    def __verifyMove(self,move):
        i,j = move.row,move.col

        if self.emptySlots == 0:
            raise Exception("Game is already finished")
        
        if move.player.id != self.p1.id and self.turn:
            raise Exception("Recieved Move from invalid player")

        if move.player.id != self.p2.id and not self.turn:
            raise Exception("Recieved Move from invalid player")

        if (self.turn and move.player == self.p2) or (not self.turn and move.player == self.p1):
            raise Exception("Wrong player turn")

        if move.row >= 3:
            raise Exception("Invalid move in row")

        if move.col >= 3:
            raise Exception("Invalid move in col")
        
        if self.board[i][j] != 0:
            raise Exception("Board is already filled at location")

    def makeMove(self,move:Move):

        self.__verifyMove(move)
        i,j = move.row,move.col
        p = 1 if self.p1 == move.player else -1
        
        self.board[i][j] = p
        self.rowC[i] += p
        self.colC[j] += p
        if i == j:
            self.upperDiagC += p
        
        if i == 3 - i - 1:
            self.loweDiagC += p
        
        res = self.__checkWinner(i,j)
        if res:
            self.gameStatus =  GameStatus.First if self.turn else GameStatus.Second
        else:
            if self.emptySlots == 0:
                self.gameStatus = GameStatus.Draw

        self.turn = not self.turn
        self.emptySlots -= 1


class Game:
    def __init__(self,p1,p2) -> None:
        self.gameId = uuid.uuid4()
        self.__board = Board(p1,p2)
        self.p1 = p1
        self.p2 = p2
        self.moves = []

    @property
    def __getStatus(self):
        if self.__board.gameStatus == GameStatus.First:
            p1.stats.updateStats(True)
            p2.stats.updateStats(False)
            print(p1.name + " Has won the game ")
            return False
        if self.__board.gameStatus == GameStatus.Second:
            p1.stats.updateStats(False)
            p2.stats.updateStats(True)
            print(p2.name + " Has won the game ")
            return False
        if self.__board.gameStatus == GameStatus.Draw:
            print("Game is Draw")
            return False
        if self.__board.gameStatus == GameStatus.Unfinished:
            print("Game is ongoing")
            return True

    def refreshBoard(self):
        self.__board = Board(self.p1,self.p2)

    @property
    def printCurrentBoard(self):
        return self.__board.printBoard()

    def makeMove(self,move):
        try:
            if not self.__getStatus:
                return
            self.__board.makeMove(move)
            self.moves.append(move)    
            self.printCurrentBoard    
        except Exception as e:
            print(e.args)
    
        
    

p1 = User("Ankit")
p2 = User("Sumit")
g = Game(p1,p2)

g.makeMove(Move(0,1,p1))
g.makeMove(Move(1,1,p2))
g.makeMove(Move(2,1,p1))
g.makeMove(Move(0,0,p2))
g.makeMove(Move(0,2,p1))
g.makeMove(Move(2,2,p2))
g.makeMove(Move(22,22,p1))
g.refreshBoard()
g.makeMove(Move(1,1,p1))
g.makeMove(Move(0,1,p2))
g.makeMove(Move(0,0,p1))
g.makeMove(Move(2,1,p2))
g.makeMove(Move(2,2,p1))
g.makeMove(Move(0,2,p2))
g.makeMove(Move(22,22,p1))
print(p2.stats.getWinRate)
