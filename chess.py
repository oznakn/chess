from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessMove import ChessMove

chessMap = ChessMap()
chessMap.selectPiece(chessMap.pwc("B1"))
chessMap.printMap()

chessMove = ChessMove(chessMap)

print chessMove.getAvaliablePoints()