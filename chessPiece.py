from constants import *

class ChessPiece:
	def __init__(self, point, pieceType, player):
		self.point = point
		self.pieceType = pieceType
		self.player = player
		
	def duplicate(self):
		newChessPiece = ChessPiece(self.point, self.pieceType, self.player)
		return newChessPiece
		
	def pieceTypeToString(self):
		part1 = ""
		part2 = ""

		if self.player == PLAYER_BLACK :
			part1 = "B"
		elif self.player == PLAYER_WHITE :
			part1 = "W"
			
		if self.pieceType == PIECE_KING:
			part2 = "K"
		elif self.pieceType == PIECE_ROOK:
			part2 = "R"
		elif self.pieceType == PIECE_BISHOP:
			part2 = "B"
		elif self.pieceType == PIECE_QUEEN:
			part2 = "Q"
		elif self.pieceType == PIECE_KNIGHT:
			part2 = "N"
		elif self.pieceType == PIECE_PAWN:
			part2 = "P"
					
		return part1 + "_" + part2
