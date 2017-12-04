from constants import *
from printColors import PrintColors
from chessPiece import ChessPiece

class ChessMap:
	#map[8][8]
	
	def __init__(self):
		self.selectedPiece = None
		self.map = []
		
		for y in range(0,8):
			mapRow = []
			
			for x in range(0,8):
				mapRow.append(None)
				
			self.map.append(mapRow)
			
		self.__init()
			
	def __init(self):
		self.add(ChessPiece((0,7), PIECE_ROOK,   PLAYER_WHITE))
		self.add(ChessPiece((1,7), PIECE_KNIGHT, PLAYER_WHITE))
		self.add(ChessPiece((2,7), PIECE_BISHOP, PLAYER_WHITE))
		self.add(ChessPiece((3,7), PIECE_QUEEN,  PLAYER_WHITE))
		self.add(ChessPiece((4,7), PIECE_KING,   PLAYER_WHITE))
		self.add(ChessPiece((5,7), PIECE_BISHOP, PLAYER_WHITE))
		self.add(ChessPiece((6,7), PIECE_KNIGHT, PLAYER_WHITE))
		self.add(ChessPiece((7,7), PIECE_ROOK,   PLAYER_WHITE))
		
		self.add(ChessPiece((0,0), PIECE_ROOK,   PLAYER_BLACK))
		self.add(ChessPiece((1,0), PIECE_KNIGHT, PLAYER_BLACK))
		self.add(ChessPiece((2,0), PIECE_BISHOP, PLAYER_BLACK))
		self.add(ChessPiece((3,0), PIECE_QUEEN,  PLAYER_BLACK))
		self.add(ChessPiece((4,0), PIECE_KING,   PLAYER_BLACK))
		self.add(ChessPiece((5,0), PIECE_BISHOP, PLAYER_BLACK))
		self.add(ChessPiece((6,0), PIECE_KNIGHT, PLAYER_BLACK))
		self.add(ChessPiece((7,0), PIECE_ROOK,   PLAYER_BLACK))
		
		for i in range(0,8):
			self.add(ChessPiece((i,6), PIECE_PAWN, PLAYER_WHITE))
			self.add(ChessPiece((i,1), PIECE_PAWN, PLAYER_BLACK))
			
	def add(self, chessPiece): 
		self.map[chessPiece.point[0]][chessPiece.point[1]] = chessPiece
			
	def get(self, point):
		return self.map[point[0]][point[1]]
		
	def gwc(self, input): #get with code
		return self.get(self.pwc(input))
		
	def pwc(self, input): #pick with code
		input = str(input).lower()
		
		x = str(input[0])
		y = str(input[1])
		
		if x == "a":
			x = 0
		elif x == "b":
			x = 1
		elif x == "c":
			x = 2
		elif x == "d":
			x = 3
		elif x == "e":
			x = 4
		elif x == "f":
			x = 5
		elif x == "g":
			x = 6
		elif x == "h":
			x = 7
			
		y = int(y)
		y = 8 - y
		
		return (x,y)
			
	def isPointEmpty(self, point):
		return self.map[point[0]][point[1]] == None
		
	def selectPiece(self, point):
		self.selectedPiece = self.get(point)
	
	def deselectPiece(self):
		self.selectedPiece = None

	def validate(self):
		#king, queen, rook, bishop, knigt, pawn
		whiteList = [0,0,0,0,0,0]
		blackList = [0,0,0,0,0,0]
		
		for y in range(0,8):
			for x in range(0,8):
				chessPiece = self.map[x][y]
				
				if chessPiece != None:
					if chessPiece.player == PLAYER_WHITE:
						if chessPiece.pieceType == PIECE_KING:
							whiteList[0] += 1
						elif chessPiece.pieceType == PIECE_QUEEN:
							whiteList[1] += 1
						elif chessPiece.pieceType == PIECE_ROOK:
							whiteList[2] += 1
						elif chessPiece.pieceType == PIECE_BISHOP:
							whiteList[3] += 1
						elif chessPiece.pieceType == PIECE_KNIGHT:
							whiteList[4] += 1
						elif chessPiece.pieceType == PIECE_PAWN:
							whiteList[5] += 1
					elif chessPiece.player == PLAYER_BLACK:
						if chessPiece.pieceType == PIECE_KING:
							blackList[0] += 1
						elif chessPiece.pieceType == PIECE_QUEEN:
							blackList[1] += 1
						elif chessPiece.pieceType == PIECE_ROOK:
							blackList[2] += 1
						elif chessPiece.pieceType == PIECE_BISHOP:
							blackList[3] += 1
						elif chessPiece.pieceType == PIECE_KNIGHT:
							blackList[4] += 1
						elif chessPiece.pieceType == PIECE_PAWN:
							blackList[5] += 1
		
		whiteValue = whiteList[0] == 1 and whiteList[1] == 1 and whiteList[2] == 2 and whiteList[3] == 2 and whiteList[4] == 2 and whiteList[5] == 8
		blackValue = blackList[0] == 1 and blackList[1] == 1 and blackList[2] == 2 and blackList[3] == 2 and blackList[4] == 2 and blackList[5] == 8
		
		return whiteValue and blackValue

	def move(self, start, finish): 
		tempPiece = self.get(start)
		
		if tempPiece != None:
			self.map[start[0]][start[1]] = None
			self.map[finish[0]][finish[1]] = tempPiece
		
	def printMap(self):
		print ""
		print "       A      B      C      D      E      F      G      H   "
		print "   ---------------------------------------------------------   "
		
		for y in range(0,8):
			printLine = str(8 - y) +  "  | "
			for x in range(0,8):
				chessPiece = self.map[x][y]
				
				if chessPiece != None :
					if self.selectedPiece != None and self.selectedPiece.point == chessPiece.point :
						printLine += PrintColors.UNDERLINE + chessPiece.pieceTypeToString() + PrintColors.ENDC
					else :
						printLine += chessPiece.pieceTypeToString()
				else :
					printLine += "    "
					
				printLine += " | "
				
			printLine += str(8 - y)
			
			print printLine
			print "   ---------------------------------------------------------   "

		print "       A      B      C      D      E      F      G      H   "
		print ""
