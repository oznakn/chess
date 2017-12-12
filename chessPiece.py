from constants import *

class ChessPiece:
	def __init__(self, point, pieceType, player):
		self.point = point
		self.pieceType = pieceType
		self.player = player
		self.moves = []

	def __getAvailableMoves(self, chessMap, factor, distance = -1):
		availablePoints = []

		if distance == -1:
			distance = 7

		distance += 1

		if self.pieceType == PIECE_PAWN:
			if 0 <= self.point[1] + factor[1] < 8 : # normal move
				if chessMap.get((self.point[0], self.point[1] + factor[1])) == None:
					availablePoints.append((self.point[0], self.point[1] + factor[1]))

				if 0 <= self.point[0] + 1 < 8: # take move right
					tempChessPiece = chessMap.get((self.point[0] + 1, self.point[1] + factor[1]))

					if tempChessPiece != None and tempChessPiece.player != self.player:
						availablePoints.append((self.point[0] + 1, self.point[1] + factor[1]))

				if 0 <= self.point[0] - 1 < 8: # take move left
					tempChessPiece = chessMap.get((self.point[0] - 1, self.point[1] + factor[1]))

					if tempChessPiece != None and tempChessPiece.player != self.player:
						availablePoints.append((self.point[0] - 1, self.point[1] + factor[1]))

				if (factor[1] == 1 and self.point[1] == 1) or (factor[1] == -1 and self.point[1] == 6): #white first move pawn || black first move span
					tempFactor = factor[1] * 2

					if 0 <= self.point[1] + tempFactor < 8 : # normal first move
						availablePoints.append((self.point[0], self.point[1] + tempFactor))

		else:
			for i in range(1,distance):
				if 0 <= self.point[0] + (factor[0] * i) < 8 and 0 <= self.point[1] + (factor[1] * i) < 8 :
					point = (self.point[0] + (factor[0] * i), self.point[1] + (factor[1] * i))

					if chessMap.isPointEmpty(point) == True:
						availablePoints.append(point)
					else :
						if chessMap.get(point).player != self.player :
							availablePoints.append(point)

						if self.pieceType != PIECE_KNIGHT :
							break
				else :
					break

		return availablePoints

	def generateMoves(self, chessMap):
		self.moves = []

		if self.pieceType == PIECE_KING :
			self.moves += self.__getAvailableMoves(chessMap, (1,1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (1,-1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-1,1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-1,-1), 1)

			self.moves += self.__getAvailableMoves(chessMap, (1,0), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-1,0), 1)
			self.moves += self.__getAvailableMoves(chessMap, (0,1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (0,-1), 1)

		elif self.pieceType == PIECE_QUEEN :
			self.moves += self.__getAvailableMoves(chessMap, (1,1))
			self.moves += self.__getAvailableMoves(chessMap, (1,-1))
			self.moves += self.__getAvailableMoves(chessMap, (-1,1))
			self.moves += self.__getAvailableMoves(chessMap, (-1,-1))

			self.moves += self.__getAvailableMoves(chessMap, (1,0))
			self.moves += self.__getAvailableMoves(chessMap, (-1,0))
			self.moves += self.__getAvailableMoves(chessMap, (0,1))
			self.moves += self.__getAvailableMoves(chessMap, (0,-1))

		elif self.pieceType == PIECE_ROOK :
			self.moves += self.__getAvailableMoves(chessMap, (1,0))
			self.moves += self.__getAvailableMoves(chessMap, (-1,0))
			self.moves += self.__getAvailableMoves(chessMap, (0,1))
			self.moves += self.__getAvailableMoves(chessMap, (0,-1))

		elif self.pieceType == PIECE_BISHOP :
			self.moves += self.__getAvailableMoves(chessMap, (1,1))
			self.moves += self.__getAvailableMoves(chessMap, (1,-1))
			self.moves += self.__getAvailableMoves(chessMap, (-1,1))
			self.moves += self.__getAvailableMoves(chessMap, (-1,-1))

		elif self.pieceType == PIECE_KNIGHT :
			self.moves += self.__getAvailableMoves(chessMap, (2,1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (2,-1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-2,1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-2,-1), 1)
			self.moves += self.__getAvailableMoves(chessMap, (1,2), 1)
			self.moves += self.__getAvailableMoves(chessMap, (1,-2), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-1,2), 1)
			self.moves += self.__getAvailableMoves(chessMap, (-1,-2), 1)

		elif self.pieceType == PIECE_PAWN :
			if self.player == PLAYER_WHITE:
				self.moves += self.__getAvailableMoves(chessMap, (0,1), 1)

			elif self.player == PLAYER_BLACK:
				self.moves += self.__getAvailableMoves(chessMap, (0,-1),  1)

	def duplicate(self):
		newChessPiece = ChessPiece(self.point, self.pieceType, self.player)

		newChessPiece.moves = self.moves[:]

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
