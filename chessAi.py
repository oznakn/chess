import timeit
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessMove import ChessMove

counterValue = 0

def counter():
	global counterValue
	counterValue += 1

class Node:
	def __init__(self, chessMap, mark, player, deep):
		counter()
		self.chessMap = chessMap
		self.filteredMap = chessMap.filterMap(player)
		
		self.mark = mark
		self.player = player
		self.deep = deep
		
		self.childNodes = []

	def run(self):
		newPlayer = PLAYER_BLACK
		if self.player == PLAYER_BLACK:
			newPlayer = PLAYER_WHITE
		
		for chessPiece in self.filteredMap:
			if chessPiece != None:
				chessMove = ChessMove(self.chessMap, chessPiece)
				moves = chessMove.getAvailableMoves()
				
				for move in moves:
					newChessMap = self.chessMap.duplicate()

					chessMove.chessMap = newChessMap
					chessMove.apply(move, True)
					
					mark = chessMove.calculateMark(move)
					
					if chessPiece.player == PLAYER_BLACK:
						mark *= -1
						
					if self.deep <= 1:
						node = Node(newChessMap, mark, newPlayer, self.deep + 1)
						self.childNodes.append(node)
						node.run()
							
#	def calculate(self):
#		resultMark = self.mark
#		
#		for node in self.childNodes:
#			resultMark += node.calculate()
#		
#		return resultMark

class ChessAI:
	def __init__(self, chessMap):
		self.chessMap = chessMap

	def alphabeta(self, node, depth, alpha, beta, player):
		if depth == 0:
			return node.mark
			
		if player == PLAYER_WHITE:
			value = -9999999
			for child in node.childNodes:
				value = max(value, self.alphabeta(child, depth - 1, alpha, beta, PLAYER_BLACK))
				alpha = max(alpha, value)
				
				if beta <= alpha:
					break
			return value
		else:
			value = 9999999
			for child in node.childNodes:
				value = min(value, self.alphabeta(child, depth - 1, alpha, beta, PLAYER_WHITE))
				beta  = min(beta, value)
				
				if beta <= alpha:
					break
			return value

	def run(self):
		
		start = timeit.default_timer()
		
		node = Node(self.chessMap, 0,PLAYER_BLACK, 0)
		node.run()

		stop = timeit.default_timer()

		print stop - start 
		start = timeit.default_timer()
		
		bestOptionForNode = node.childNodes[0]
		bestValueForNode = self.alphabeta(bestOptionForNode, 2, -9999999, 9999999, PLAYER_BLACK)
		
		for i in range(1, len(node.childNodes)):
			calculated = self.alphabeta(node.childNodes[i], 2, -9999999, 9999999, PLAYER_BLACK)
			
			if calculated >= bestValueForNode:
				bestOptionForNode = node.childNodes[i]
				bestValueForNode = calculated
		
		stop = timeit.default_timer()
		print stop - start
		global counterValue		
		print counterValue
		return bestOptionForNode
						
						