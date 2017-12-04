from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessMove import ChessMove

class ChessAI:
	def __init__(self, chessMap, player, turn):
		self.chessMap = chessMap
		self.player = player
		self.turn = turn
	
	def run(self):
		if self.turn == self.player:
			return 0