from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap

class ChessMove:
	def __init__(self, chessMap, chessPiece = None):
		if chessPiece == None:
			chessPiece = chessMap.selectedPiece
			
		self.chessMap = chessMap	
		self.chessPiece = chessPiece
		self.avaliablePoints = None
		
	def __getAvaliablePoints(self, factor, distance = -1): 
		avaliablePoints = []
		
		if distance == -1:
			distance = 7
			
		distance += 1
		
		if self.chessPiece.pieceType == PIECE_PAWN:
			if 0 <= self.chessPiece.point[1] + factor[1] < 8 : # normal move
				avaliablePoints.append((self.chessPiece.point[0], self.chessPiece.point[1] + factor[1]))
				
				if 0 <= self.chessPiece.point[0] + 1 < 8: # take move right
					tempChessPiece = self.chessMap.get((self.chessPiece.point[0] + 1, self.chessPiece.point[1] + factor[1]))
					
					if tempChessPiece != None and tempChessPiece.player != self.chessPiece.player:
						avaliablePoints.append((self.chessPiece.point[0] + 1, self.chessPiece.point[1] + factor[1]))
						
				if 0 <= self.chessPiece.point[0] - 1 < 8: # take move left
					tempChessPiece = self.chessMap.get((self.chessPiece.point[0] - 1, self.chessPiece.point[1] + factor[1]))
					
					if tempChessPiece != None and tempChessPiece.player != self.chessPiece.player:
						avaliablePoints.append((self.chessPiece.point[0] - 1, self.chessPiece.point[1] + factor[1]))
			
				if (factor[1] == 1 and self.chessPiece.point[1] == 1) or (factor[1] == -1 and self.chessPiece.point[1] == 7): #white first move pawn || black first move span
					tempFactor = factor[1] * 2
				
					if 0 <= self.chessPiece.point[1] + tempFactor < 8 : # normal first move
						avaliablePoints.append((self.chessPiece.point[0], self.chessPiece.point[1] + tempFactor))
		
		else:
			for i in range(1,distance):
				if 0 <= self.chessPiece.point[0] + (factor[0] * i) < 8 and 0 <= self.chessPiece.point[1] + (factor[1] * i) < 8 :
					point = (self.chessPiece.point[0] + (factor[0] * i), self.chessPiece.point[1] + (factor[1] * i))
					
					if self.chessMap.isPointEmpty(point) == True:
						avaliablePoints.append(point)
					else :
						if self.chessMap.get(point).player != self.chessPiece.player :
							avaliablePoints.append(point)
						
						if self.chessPiece.pieceType != PIECE_KNIGHT :
							break
				else :
					break

		return avaliablePoints
		
	def getAvaliablePoints(self):
		avaliablePoints = []

		if self.chessPiece.pieceType == PIECE_KING :
			avaliablePoints += self.__getAvaliablePoints((1,1), 1)
			avaliablePoints += self.__getAvaliablePoints((1,-1), 1)
			avaliablePoints += self.__getAvaliablePoints((-1,1), 1)
			avaliablePoints += self.__getAvaliablePoints((-1,-1), 1)
			
			avaliablePoints += self.__getAvaliablePoints((1,0), 1)
			avaliablePoints += self.__getAvaliablePoints((-1,0), 1)
			avaliablePoints += self.__getAvaliablePoints((0,1), 1)
			avaliablePoints += self.__getAvaliablePoints((0,-1), 1)
		
		elif self.chessPiece.pieceType == PIECE_QUEEN :
			avaliablePoints += self.__getAvaliablePoints((1,1))
			avaliablePoints += self.__getAvaliablePoints((1,-1))
			avaliablePoints += self.__getAvaliablePoints((-1,1))
			avaliablePoints += self.__getAvaliablePoints((-1,-1))
			
			avaliablePoints += self.__getAvaliablePoints((1,0))
			avaliablePoints += self.__getAvaliablePoints((-1,0))
			avaliablePoints += self.__getAvaliablePoints((0,1))
			avaliablePoints += self.__getAvaliablePoints((0,-1))
		
		elif self.chessPiece.pieceType == PIECE_ROOK :
			avaliablePoints += self.__getAvaliablePoints((1,0))
			avaliablePoints += self.__getAvaliablePoints((-1,0))
			avaliablePoints += self.__getAvaliablePoints((0,1))
			avaliablePoints += self.__getAvaliablePoints((0,-1))
			
		elif self.chessPiece.pieceType == PIECE_BISHOP :
			avaliablePoints += self.__getAvaliablePoints((1,1))
			avaliablePoints += self.__getAvaliablePoints((1,-1))
			avaliablePoints += self.__getAvaliablePoints((-1,1))
			avaliablePoints += self.__getAvaliablePoints((-1,-1))
		
		elif self.chessPiece.pieceType == PIECE_KNIGHT :
			avaliablePoints += self.__getAvaliablePoints((2,1), 1)
			avaliablePoints += self.__getAvaliablePoints((2,-1), 1)
			avaliablePoints += self.__getAvaliablePoints((-2,1), 1)
			avaliablePoints += self.__getAvaliablePoints((-2,-1), 1)
			avaliablePoints += self.__getAvaliablePoints((1,2), 1)
			avaliablePoints += self.__getAvaliablePoints((1,-2), 1)
			avaliablePoints += self.__getAvaliablePoints((-1,2), 1)
			avaliablePoints += self.__getAvaliablePoints((-1,-2), 1)
			
		elif self.chessPiece.pieceType == PIECE_PAWN :
			if self.chessPiece.player == PLAYER_WHITE:
				avaliablePoints += self.__getAvaliablePoints((0,-1), 1)
				
			elif self.chessPiece.player == PLAYER_BLACK:
				avaliablePoints += self.__getAvaliablePoints((0,1),  1)
	
		self.avaliablePoints = avaliablePoints
		return avaliablePoints
		
	def apply(self, point, chessMap):
		if self.avaliablePoints == None :
			self.avaliablePoints = self.getAvaliablePoints()
		
		avaliablePoints = self.avaliablePoints
		
		if point in avaliablePoints:
			chessMap.move(self.chessPiece.point, point)
		