from constants import *

class ChessPiece:
	def __init__(self, point, pieceType, player):
		self.point = point
		self.pieceType = pieceType
		self.player = player
		
	def pieceTypeToString(self):
		part1 = ""
		part2 = ""

		if self.player == PLAYER_BLACK :
			part1 = "B"
		elif self.player == PLAYER_WHITE :
			part1 = "W"
			
		if self.pieceType == PIECE_KING:
			part2 = "KI"
		elif self.pieceType == PIECE_ROOK:
			part2 = "RO"
		elif self.pieceType == PIECE_BISHOP:
			part2 = "BI"
		elif self.pieceType == PIECE_QUEEN:
			part2 = "QU"
		elif self.pieceType == PIECE_KNIGHT:
			part2 = "KN"
		elif self.pieceType == PIECE_PAWN:
			part2 = "PA"
					
		return part1 + "_" + part2
