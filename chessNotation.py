import math
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessMove import ChessMove

class ChessNotation:
	def __init__(self, chessMap):
		self.chessMap = chessMap
		
	def findDistanceSquare(self, point1, point2):
		return math.pow(math.fabs(point1[0] - point2[0]), 2) + math.pow(math.fabs(point1[1] - point2[1]), 2)
	
	def findClosest(self, filteredMap, point):
		best = filteredMap[0]

		if len(filteredMap) > 1:
			bestValue = self.findDistanceSquare(best.point, point)
			
			for i in range(1, len(filteredMap)):
				if bestValue > self.findDistanceSquare(filteredMap[i].point, point):
					best = filteredMap[i]
					bestValue = self.findDistanceSquare(filteredMap[i].point, point)

		return best
		
	def filterForPieces(self, pieceType, player):
		return self.chessMap.filterMap(pieceType, player)
		
	def filterForMoves(self, filteredMap, point):
		resultFilteredMap = []

		for piece in filteredMap:
			chessMove = ChessMove(self.chessMap, piece)
			
			if point in chessMove.getAvailableMoves():
				resultFilteredMap.append(piece)

		return resultFilteredMap

	def filterForClosestClue(self, filteredMap, closestClue):
		if closestClue == None:
			return filteredMap

		resultFilteredMap = []

		for item in filteredMap:
			if item.point[0] == self.chessMap.pwcx(closestClue):
				resultFilteredMap.append(item)

		return resultFilteredMap
	
	def applyWithPiece(self, point, pieceType, player, capturePermission, closestClue = None):
		filteredMap = self.filterForPieces(pieceType, player)
		filteredMap = self.filterForMoves(filteredMap, point)

		if len(filteredMap) > 0:
			filteredMap = self.filterForClosestClue(filteredMap, closestClue)

			if len(filteredMap) > 0:
				closest = filteredMap[0]

				if len(filteredMap) != 1:
					closest = self.findClosest(filteredMap, point)

				chessMove = ChessMove(self.chessMap, closest)
				
				return chessMove.apply(point, capturePermission)
		
		return False
	
	def isPieceCodeExceptPawn(self, input):
		input = str(input)
		if input == "K" or input == "Q" or input == "B" or input == "R" or input == "N":
			return True

		return False
	
	def apply(self, input, player):
		if len(input) == 4: # capture
			firstLetter = str(input[0])
			point = self.chessMap.pwc(input[-2:])

			if self.isPieceCodeExceptPawn(firstLetter) and str(input[1] == "x"):
				if firstLetter == "K":
					return self.applyWithPiece(point, PIECE_KING, player, True)
				elif firstLetter == "Q":
					return self.applyWithPiece(point, PIECE_QUEEN, player, True)
				elif firstLetter == "B":
					return self.applyWithPiece(point, PIECE_BISHOP, player, True)
				elif firstLetter == "R":
					return self.applyWithPiece(point, PIECE_ROOK, player, True)
				elif firstLetter == "N":
					return self.applyWithPiece(point, PIECE_KNIGHT, player, True)

			elif str(input[1] == "x"): #pawn hasCapturePermission
				return self.applyWithPiece(point, PIECE_PAWN, player, True, str(input[0]))

		elif len(input) == 3: #nocapture
			firstLetter = str(input[0])
			point = self.chessMap.pwc(input[-2:])

			if self.isPieceCodeExceptPawn(firstLetter):
				if firstLetter == "K":
					return self.applyWithPiece(point, PIECE_KING, player, False)
				elif firstLetter == "Q":
					return self.applyWithPiece(point, PIECE_QUEEN, player, False)
				elif firstLetter == "B":
					return self.applyWithPiece(point, PIECE_BISHOP, player, False)
				elif firstLetter == "R":
					return self.applyWithPiece(point, PIECE_ROOK, player, False)
				elif firstLetter == "N":
					return self.applyWithPiece(point, PIECE_KNIGHT, player, False)

		elif len(input) == 2: #just pawn
			point = self.chessMap.pwc(input)
			return self.applyWithPiece(point, PIECE_PAWN, player, False)

		return False

