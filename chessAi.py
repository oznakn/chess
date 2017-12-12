import time
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap

class Node:
	def __init__(self, chessMap, whichFor, player, deep, mainMove):
		self.chessMap = chessMap
		self.filteredMap = chessMap.filterMap((None, player))
		self.mainMove = mainMove

		self.whichFor = whichFor
		self.player = player
		self.deep = deep

		self.childNodes = []

		self.mark = self.chessMap.calculateMark(self.whichFor)

	def run(self):
		if self.deep <= 2:
			newPlayer = PLAYER_BLACK
			if self.player == PLAYER_BLACK:
				newPlayer = PLAYER_WHITE

			for chessPiece in self.filteredMap:
				for move in chessPiece.moves:
					newChessMap = self.chessMap.duplicate()

					moveObject = newChessMap.move(chessPiece.point, move, True)

					node = Node(newChessMap, self.whichFor, newPlayer, self.deep + 1, moveObject)

					self.childNodes.append(node)

					node.run()

class ChessAI:
	def __init__(self, chessMap, whichFor):
		self.whichFor = whichFor
		self.chessMap = chessMap

	def alphabeta(self, node, depth, alpha, beta, player):
		if depth == 0 or len(node.childNodes) == 0:
			return node.mark

		newPlayer = PLAYER_BLACK
		if player == PLAYER_BLACK:
			newPlayer = PLAYER_WHITE

		if player == self.whichFor:
			value = -9999999
			for child in node.childNodes:
				value = max(value, self.alphabeta(child, depth - 1, alpha, beta, newPlayer))
				alpha = max(alpha, value)

				if beta <= alpha:
					break
			return value
		else:
			value = 9999999
			for child in node.childNodes:
				value = min(value, self.alphabeta(child, depth - 1, alpha, beta, newPlayer))
				beta  = min(beta, value)

				if beta <= alpha:
					break
			return value

	def run(self):
		#startTime = time.time()
		node = Node(self.chessMap, self.whichFor, self.whichFor, 0, None)
		node.run()
		#print time.time() - startTime
		#startTime = time.time()
		bestOptionForNode = node.childNodes[0]
		bestValueForNode = self.alphabeta(bestOptionForNode, 2, -999999, 9999999, self.whichFor)

		for i in range(1, len(node.childNodes)):
			calculated = self.alphabeta(node.childNodes[i], 2, -9999999, 9999999, self.whichFor)

			if calculated >= bestValueForNode:
				bestOptionForNode = node.childNodes[i]
				bestValueForNode = calculated
		#print time.time() - startTime
		#print " "
		return bestOptionForNode

