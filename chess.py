import os
import sys
from constants import *
from chessPiece import ChessPiece
from chessMap import ChessMap
from chessMove import ChessMove
from chessNotation import ChessNotation

def cursorToTop():
#	sys.stdout.write("\033[F")
	os.system('cls' if os.name == 'nt' else 'clear')

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

while True:
	cursorToTop()
	print "PlayersTurn:", whoseTurn(player)
	
	print " "
	for inputItem in inputs[-8:]:
		print str(inputs.index(inputItem)+1) + ". " + inputItem
	
	chessMap.printMap()
	
	input = raw_input()
	
	chessNotation = ChessNotation(chessMap)	
	
	if chessNotation.apply(input, player):
		inputs.append(input)
		player = changePlayer(player)
		
	print " "
	print " "