from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap

class ChessMove:
	def __init__(self, chessMap, chessPiece = None):
		if chessPiece == None:
			chessPiece = chessMap.selectedPiece
			
		self.chessMap = chessMap	
		self.chessPiece = chessPiece
		self.availablePoints = None
		
	def __getAvailableMoves(self, factor, distance = -1): 
		availablePoints = []
		
		if distance == -1:
			distance = 7
			
		distance += 1
		
		if self.chessPiece.pieceType == PIECE_PAWN:
			if 0 <= self.chessPiece.point[1] + factor[1] < 8 : # normal move
				availablePoints.append((self.chessPiece.point[0], self.chessPiece.point[1] + factor[1]))
				
				if 0 <= self.chessPiece.point[0] + 1 < 8: # take move right
					tempChessPiece = self.chessMap.get((self.chessPiece.point[0] + 1, self.chessPiece.point[1] + factor[1]))
					
					if tempChessPiece != None and tempChessPiece.player != self.chessPiece.player:
						availablePoints.append((self.chessPiece.point[0] + 1, self.chessPiece.point[1] + factor[1]))
						
				if 0 <= self.chessPiece.point[0] - 1 < 8: # take move left
					tempChessPiece = self.chessMap.get((self.chessPiece.point[0] - 1, self.chessPiece.point[1] + factor[1]))
					
					if tempChessPiece != None and tempChessPiece.player != self.chessPiece.player:
						availablePoints.append((self.chessPiece.point[0] - 1, self.chessPiece.point[1] + factor[1]))
			
				if (factor[1] == 1 and self.chessPiece.point[1] == 1) or (factor[1] == -1 and self.chessPiece.point[1] == 6): #white first move pawn || black first move span
					tempFactor = factor[1] * 2
				
					if 0 <= self.chessPiece.point[1] + tempFactor < 8 : # normal first move
						availablePoints.append((self.chessPiece.point[0], self.chessPiece.point[1] + tempFactor))
		
		else:
			for i in range(1,distance):
				if 0 <= self.chessPiece.point[0] + (factor[0] * i) < 8 and 0 <= self.chessPiece.point[1] + (factor[1] * i) < 8 :
					point = (self.chessPiece.point[0] + (factor[0] * i), self.chessPiece.point[1] + (factor[1] * i))
					
					if self.chessMap.isPointEmpty(point) == True:
						availablePoints.append(point)
					else :
						if self.chessMap.get(point).player != self.chessPiece.player :
							availablePoints.append(point)
						
						if self.chessPiece.pieceType != PIECE_KNIGHT :
							break
				else :
					break

		return availablePoints
		
	def getAvailableMoves(self):
		availablePoints = []

		if self.chessPiece.pieceType == PIECE_KING :
			availablePoints += self.__getAvailableMoves((1,1), 1)
			availablePoints += self.__getAvailableMoves((1,-1), 1)
			availablePoints += self.__getAvailableMoves((-1,1), 1)
			availablePoints += self.__getAvailableMoves((-1,-1), 1)
			
			availablePoints += self.__getAvailableMoves((1,0), 1)
			availablePoints += self.__getAvailableMoves((-1,0), 1)
			availablePoints += self.__getAvailableMoves((0,1), 1)
			availablePoints += self.__getAvailableMoves((0,-1), 1)
		
		elif self.chessPiece.pieceType == PIECE_QUEEN :
			availablePoints += self.__getAvailableMoves((1,1))
			availablePoints += self.__getAvailableMoves((1,-1))
			availablePoints += self.__getAvailableMoves((-1,1))
			availablePoints += self.__getAvailableMoves((-1,-1))
			
			availablePoints += self.__getAvailableMoves((1,0))
			availablePoints += self.__getAvailableMoves((-1,0))
			availablePoints += self.__getAvailableMoves((0,1))
			availablePoints += self.__getAvailableMoves((0,-1))
		
		elif self.chessPiece.pieceType == PIECE_ROOK :
			availablePoints += self.__getAvailableMoves((1,0))
			availablePoints += self.__getAvailableMoves((-1,0))
			availablePoints += self.__getAvailableMoves((0,1))
			availablePoints += self.__getAvailableMoves((0,-1))
			
		elif self.chessPiece.pieceType == PIECE_BISHOP :
			availablePoints += self.__getAvailableMoves((1,1))
			availablePoints += self.__getAvailableMoves((1,-1))
			availablePoints += self.__getAvailableMoves((-1,1))
			availablePoints += self.__getAvailableMoves((-1,-1))
		
		elif self.chessPiece.pieceType == PIECE_KNIGHT :
			availablePoints += self.__getAvailableMoves((2,1), 1)
			availablePoints += self.__getAvailableMoves((2,-1), 1)
			availablePoints += self.__getAvailableMoves((-2,1), 1)
			availablePoints += self.__getAvailableMoves((-2,-1), 1)
			availablePoints += self.__getAvailableMoves((1,2), 1)
			availablePoints += self.__getAvailableMoves((1,-2), 1)
			availablePoints += self.__getAvailableMoves((-1,2), 1)
			availablePoints += self.__getAvailableMoves((-1,-2), 1)
			
		elif self.chessPiece.pieceType == PIECE_PAWN :
			if self.chessPiece.player == PLAYER_WHITE:
				availablePoints += self.__getAvailableMoves((0,-1), 1)
				
			elif self.chessPiece.player == PLAYER_BLACK:
				availablePoints += self.__getAvailableMoves((0,1),  1)
	
		self.availablePoints = availablePoints
		return availablePoints
		
	def apply(self, point, capturePermission):
		if self.availablePoints == None :
			self.availablePoints = self.getAvailableMoves()
		
		availablePoints = self.availablePoints
		
		if point in availablePoints:
			return self.chessMap.move(self.chessPiece.point, point, capturePermission)
#			self.chessMap.selectedPiece = self.chessMap.get(point)
#			return True
		
		return False