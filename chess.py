# coding=utf-8
import os
import sys
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessNotation import ChessNotation
from chessAi import ChessAI

def cursorToTop():
	os.system('cls' if os.name == 'nt' else 'clear')
	return True

def whoseTurn(player):
	if player == PLAYER_WHITE:
		return "WHITE"
	else:
		return "BLACK"

def changePlayer(player):
	if player == PLAYER_BLACK:
		return PLAYER_WHITE
	else:
		return PLAYER_BLACK

inputs = []

player = PLAYER_WHITE
chessMap = ChessMap()
chessMap.init()

def printAll():
	cursorToTop()
	print "PlayersTurn:", whoseTurn(player)

	print " "
	for inputItem in inputs:
		print str(inputs.index(inputItem)+1) + ". " + inputItem

	chessMap.printMap()
	print " "
	print " "

while True:
	'''
	printAll()

	input = raw_input()

	chessNotation = ChessNotation(chessMap)

	if chessNotation.apply(input, player) != False:

	inputs.append(input)

	player = changePlayer(player)
	'''
	printAll()

	chessAi = ChessAI(chessMap, player)
	bestNode = chessAi.run()

	if bestNode.mainMove != None:
		output = str(bestNode.mainMove[0]) + " " + str(bestNode.mainMove[1])
		inputs.append(output)

	chessMap = bestNode.chessMap

	player = changePlayer(player)