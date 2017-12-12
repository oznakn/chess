from constants import *
from printColors import PrintColors
from chessPiece import ChessPiece

class ChessMap:
	#map[8][8]

	def __init__(self):
		self.pieceMap = []

		for i in range(0,8):
			newArray = []

			for j in range(0,8):
				newArray.append(None)

			self.pieceMap.append(newArray)

	def init(self):
		'''
		self.add(ChessPiece((0,0), PIECE_KNIGHT,   PLAYER_WHITE))
		self.add(ChessPiece((2,2), PIECE_KNIGHT,   PLAYER_BLACK))
		'''
		self.add(ChessPiece((0,0), PIECE_ROOK,   PLAYER_WHITE))
		self.add(ChessPiece((1,0), PIECE_KNIGHT, PLAYER_WHITE))
		self.add(ChessPiece((2,0), PIECE_BISHOP, PLAYER_WHITE))
		self.add(ChessPiece((3,0), PIECE_QUEEN,  PLAYER_WHITE))
		self.add(ChessPiece((4,0), PIECE_KING,   PLAYER_WHITE))
		self.add(ChessPiece((5,0), PIECE_BISHOP, PLAYER_WHITE))
		self.add(ChessPiece((6,0), PIECE_KNIGHT, PLAYER_WHITE))
		self.add(ChessPiece((7,0), PIECE_ROOK,   PLAYER_WHITE))

		self.add(ChessPiece((0,7), PIECE_ROOK,   PLAYER_BLACK))
		self.add(ChessPiece((1,7), PIECE_KNIGHT, PLAYER_BLACK))
		self.add(ChessPiece((2,7), PIECE_BISHOP, PLAYER_BLACK))
		self.add(ChessPiece((3,7), PIECE_QUEEN,  PLAYER_BLACK))
		self.add(ChessPiece((4,7), PIECE_KING,   PLAYER_BLACK))
		self.add(ChessPiece((5,7), PIECE_BISHOP, PLAYER_BLACK))
		self.add(ChessPiece((6,7), PIECE_KNIGHT, PLAYER_BLACK))
		self.add(ChessPiece((7,7), PIECE_ROOK,   PLAYER_BLACK))

		for i in range(0,8):
			self.add(ChessPiece((i,1), PIECE_PAWN, PLAYER_WHITE))
			self.add(ChessPiece((i,6), PIECE_PAWN, PLAYER_BLACK))

		self.calculateAllMoves()

	def add(self, chessPiece):
		self.pieceMap[chessPiece.point[0]][chessPiece.point[1]] = chessPiece

	def get(self, point):
		return self.pieceMap[point[0]][point[1]]

	def set(self, point, chessPiece):
		chessPiece.point = (point[0], point[1])

		self.pieceMap[point[0]][point[1]] = chessPiece

	def remove(self, point):
		self.pieceMap[point[0]][point[1]] = None

	def gwc(self, input): #get with code
		return self.get(self.pwc(input))

	def pwc(self, input): #pick with code
		y = str(input[1])
		y = int(y)
		y = y - 1

		return (self.pwcx(str(input[0])), y)

	def pwcx(self, x): #pick with code just x
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

		return x

	def isPointEmpty(self, point):
		return self.get(point) == None

	def move(self, fromPoint, toPoint, capturePermission):
		chessPiece = self.get(fromPoint)

		if toPoint in chessPiece.moves:
			isEmpty = self.isPointEmpty(toPoint)

			if isEmpty == True or capturePermission == True:
				self.remove(fromPoint)
				self.set(toPoint, chessPiece)

				filteredPoints = self.getChessPiecesCanGoPoint(toPoint)
				filteredPoints += self.createRangeFromPoint(toPoint, 1)
				filteredPoints += self.createRangeFromPoint(fromPoint, 1)

				filteredPoints = set(filteredPoints)
				'''
				for chessPiece in filteredPieces:
					temp = self.get(chessPiece)
					if temp != None:
						temp.generateMoves(self)

				self.calculateAllMoves()
				'''

				for x in range(0,8):
					for y in range(0,8):
						tempPiece = self.get((x,y))

						if tempPiece != None:
							tempSet = set(tempPiece.moves) & filteredPoints

							if len(tempSet) != 0 or tempPiece.point in filteredPoints:
								tempPiece.generateMoves(self)

				return (True, fromPoint, toPoint, chessPiece.pieceType, not isEmpty)

		return (False)

	def calculateMark(self, whichFor):
		mark = 0

		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.pieceMap[x][y]

				if chessPiece != None:
					factor = -1

					if whichFor == chessPiece.player:
						factor = 1

					if chessPiece.pieceType == PIECE_KING:
						mark += 900 * factor
					elif chessPiece.pieceType == PIECE_QUEEN:
						mark += 80 * factor
					elif chessPiece.pieceType == PIECE_ROOK:
						mark += 50 * factor
					elif chessPiece.pieceType == PIECE_BISHOP:
						mark += 30 * factor
					elif chessPiece.pieceType == PIECE_KNIGHT:
						mark += 30 * factor
					elif chessPiece.pieceType == PIECE_PAWN:
						mark += 10 * factor

		return mark

	def calculateAllMoves(self):
		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.pieceMap[x][y]

				if chessPiece != None:
					chessPiece.generateMoves(self)

	def getChessPiecesCanGoPoint(self, point): # pieceType, player
		resultArray = []

		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.pieceMap[x][y]

				if chessPiece != None and point in chessPiece.moves:
					resultArray.append(chessPiece.point)

		return resultArray

	def createRangeFromPoint(self, point, size):
		resultArray = []

		for x in range(size * -1, size + 1):
			for y in range(size * -1, size + 1):

				if 0 <= point[0] + x < 8 and 0 <= point[1] + y < 8:
					resultArray.append((point[0] + x, point[1] + y))

		return resultArray

	def duplicate(self):
		duplicatedChessMap = ChessMap()

		for x in range(0,8):
			for y in range(0,8):
				chessPiece = self.pieceMap[x][y]
				if chessPiece != None:
					duplicated = chessPiece.duplicate()

					duplicatedChessMap.add(duplicated)

		return duplicatedChessMap

	def filterMap(self, options = (None, None)): # pieceType, player
		resultList = []

		for y in range(0,8):
			for x in range(0,8):
				chessPiece = self.pieceMap[x][y]

				if chessPiece != None and (options[0] == None or chessPiece.pieceType == options[0]) and (options[1] == None or chessPiece.player == options[1]):
					resultList.append(chessPiece)

		return resultList

	def pointToNotationX(self, x):
		result = ""

		if x == 0:
			result += "a"
		elif x == 1:
			result += "b"
		elif x == 2:
			result += "c"
		elif x == 3:
			result += "d"
		elif x == 4:
			result += "e"
		elif x == 5:
			result += "f"
		elif x == 6:
			result += "g"
		elif x == 7:
			result += "h"

		return result

	def pieceToNotation(self, pieceType):
		result = ""

		if pieceType == PIECE_KING:
			result += "K"
		elif pieceType == PIECE_ROOK:
			result += "R"
		elif pieceType == PIECE_BISHOP:
			result += "B"
		elif pieceType == PIECE_QUEEN:
			result += "Q"
		elif pieceType == PIECE_KNIGHT:
			result += "N"

		return result

	def pointToNotation(self, point):
		result = ""

		result += self.pointToNotationX(point[0])

		result += str(point[1] + 1)

		return result

	def moveToNotation(self, fromPoint, toPoint, pieceType, hasCaptured):
		part1 = ""

		part2 = ""
		if hasCaptured == True:
			part2 = "x"

		if pieceType == PIECE_PAWN:
			if hasCaptured == True:
				part1 = self.pointToNotationX(fromPoint[0])
		else:
			part1 = self.pieceToNotation(pieceType)

		part3 = self.pointToNotation(toPoint)

		return part1 + part2 + part3

	def printMap(self):
		print "      A     B     C     D     E     F     G     H  "
		print "   -------------------------------------------------   "

		for y in range(7, -1, -1):
			printLine = str(y + 1) +  "  | "
			for x in range(0,8):
				chessPiece = self.pieceMap[x][y]

				if chessPiece != None and chessPiece.point == (x,y):
					printLine += chessPiece.pieceToPrintString()
				else :
					printLine += "   "

				printLine += " | "

			printLine += str(y + 1)

			print printLine
			print "   -------------------------------------------------   "

#		print "      0     1     2     3     4     5     6     7  "
		print "      A     B     C     D     E     F     G     H  "
		print ""
