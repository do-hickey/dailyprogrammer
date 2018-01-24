"""This module (slowly) looks for a solution to given Hue Drops Puzzles.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #347 [Hard] Hue Drops Puzzle
https://www.reddit.com/r/dailyprogrammer/comments/7riu6p/20180119_challenge_347_hard_hue_drops_puzzle/?st=jcrvclia&sh=56482508

Submitted 1/24/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import re
import copy

input_1 = '''\
4 4
W O O O
B G V R
R G B G
V O B R
O'''

input_2 = '''\
10 12
W Y O B V G V O Y B
G O O V R V R G O R
V B R R R B R B G Y
B O Y R R G Y V O V
V O B O R G B R G R
B O G Y Y G O V R V
O O G O Y R O V G G
B O O V G Y V B Y G
R B G V O R Y G G G
Y R Y B R O V O B V
O B O B Y O Y V B O
V R R G V V G V V G
V'''

colorOptions = re.findall(r'\w','R O Y G B V')
currInput = input_1

class HueBoard:
    def __init__(self,inputString):
        self.inputLines = inputString.split('\n')
        self.puzzDims = [int(i) for i in re.findall(r'\d+',self.inputLines[0])]
        self.targetColor = self.inputLines[-1]
        self.currentSet = {(0,0)}

        self.puzzMatrix = []
        for i in range(1,len(self.inputLines)-1):
            self.puzzMatrix.append(re.findall(r'\w',self.inputLines[i]))


    def printPuzz(self,lastMove):
        for line in self.puzzMatrix:
            print(*line, sep=' ')
        print(lastMove)


    def floodColors(self,newMove,commitOp):
        for tile in self.currentSet:
            if commitOp == True:
                self.puzzMatrix[tile[0]][tile[1]] = newMove

        newTiles = set()
        tempSet = copy.copy(self.currentSet)

        for x in range(max(self.puzzDims)):
            for tile in tempSet:
                adjTiles = [(tile[0]-1, tile[1]),(tile[0]+1, tile[1]),(tile[0],tile[1]-1),(tile[0],tile[1]+1)]

                for adjTile in adjTiles:
                    validTile = adjTile[0] in range(self.puzzDims[0]) and adjTile[1] in range(self.puzzDims[1])
                    try:
                        if validTile and self.puzzMatrix[adjTile[0]][adjTile[1]] == newMove:
                            newTiles.add(adjTile)
                    except IndexError:
                        continue

            for tile in newTiles:
                tempSet.add(tile)

        if commitOp == True:
            self.currentSet = self.currentSet.union(tempSet)
        else:
            return len(newTiles-self.currentSet)



def bestMove(board,moveHistory):
    tilesTaken = [0]*len(colorOptions)

    for index, color in enumerate(colorOptions):
        tilesTaken[index] = board.floodColors(color,False)
        if tilesTaken[index] == max(tilesTaken):
            bestOption = index

    #Check if the whole board is a single color
    if max(tilesTaken) == 0 and board.puzzMatrix[0][0] == board.inputLines[-1]:
        return True
    elif max(tilesTaken) == 0 and board.puzzMatrix[0][0] != board.inputLines[-1]:
        moveHistory.append(board.inputLines[-1])
        return False
    #If the whole board is not a single color, append next move
    else:
        moveHistory.append(colorOptions[bestOption])
        return False


b = HueBoard(currInput)
moveHistory = []
victoryCondition = False


while not victoryCondition:
    victoryCondition = bestMove(b,moveHistory)
    b.floodColors(moveHistory[-1],True)

#bFinished = HueBoard(currInput)
#bFinished.printPuzz(bFinished.inputLines[-1])
#for move in moveHistory:
#    bFinished.floodColors(move,True)
#    bFinished.printPuzz(move)

print(*moveHistory, sep=' ')