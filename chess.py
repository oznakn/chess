# coding=utf-8
import os
import sys
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessNotation import ChessNotation
from chessAi import ChessAI

inputs = []

player = PLAYER_WHITE
chessMap = ChessMap()
chessMap.init()

def cursorToTop():
	global inputs
	global player
	global chessMap

	os.system('cls' if os.name == 'nt' else 'clear')
	return True

def whoseTurn():
	global inputs
	global player
	global chessMap

	if player == PLAYER_WHITE:
		return "WHITE"
	else:
		return "BLACK"

def changePlayer():
	global inputs
	global player
	global chessMap

	if player == PLAYER_BLACK:
		player =  PLAYER_WHITE
	else:
		player =  PLAYER_BLACK

def printAll():
	global inputs
	global player
	global chessMap

	cursorToTop()
	print "PlayersTurn:", whoseTurn()

	print " "
	for inputItem in inputs[-8:]:
		print str(inputs.index(inputItem)+1) + ". " + inputItem

	print " "
	chessMap.printMap()
	print " "

def playerVsAI():
	global inputs
	global player
	global chessMap

	while True:
		printAll()

		input = raw_input()

		chessNotation = ChessNotation(chessMap)

		if chessNotation.apply(input, player)[0] == True:
			inputs.append(whoseTurn() + " " + input)

			changePlayer()

			printAll()

			chessAi = ChessAI(chessMap, player)
			bestNode = chessAi.run()

			if bestNode.mainMove != None and bestNode.mainMove[0] == True:
				output = chessMap.moveToNotation(bestNode.mainMove[1], bestNode.mainMove[2], bestNode.mainMove[3], bestNode.mainMove[4])

				inputs.append(whoseTurn() + " " + output)

			chessMap = bestNode.chessMap

			changePlayer()

def aiVsAI():
	global inputs
	global player
	global chessMap

	while True:
		printAll()

		chessAi = ChessAI(chessMap, player)
		bestNode = chessAi.run()

		if bestNode.mainMove != None and bestNode.mainMove[0] == True:
			output = chessMap.moveToNotation(bestNode.mainMove[1], bestNode.mainMove[2], bestNode.mainMove[3], bestNode.mainMove[4])

			inputs.append(whoseTurn() + " " + output)

		chessMap = bestNode.chessMap

		changePlayer()

#playerVsAI()
aiVsAI()