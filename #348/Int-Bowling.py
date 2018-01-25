"""This module renders the bowling frames for a given input of pins.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #348 [Intermediate] Bowling Frames Display
https://www.reddit.com/r/dailyprogrammer/comments/7so37o/20180124_challenge_348_intermediate_bowling/

Submitted 1/25/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import re

inputPins = '''\
9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0  9  0
10 10 10 10 10 10 10 10 10 10 10 10
5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5  5
10 3  7  6  1  10 10 10 2  8  9  0  7  3  10 10 10
9  0  3  7  6  1  3  7  8  1  5  5  0  10 8  0  7  3  8  2  8'''

gameList = inputPins.split('\n')
gamePins = []
for game in gameList:
    gamePins.append([int(i) for i in re.findall(r'\d+',game)])

frameRender = ['']*len(gameList)
for index,pinList in enumerate(gamePins):
    frameCounter = 1
    ballCounter = 0
    prevPins = 0

    for pin in pinList:
        #first ball
        if ballCounter == 0:
            if pin == 10:
                frameRender[index] += 'X'
                if frameCounter < 10:
                    frameCounter += 1
                    frameRender[index] += '  '
            elif pin == 0:
                frameRender[index] += '-'
                ballCounter = 1
            else:
                frameRender[index] += str(pin)
                prevPins = pin
                ballCounter = 1

        #second ball
        elif ballCounter == 1:
            if pin == 0:
                frameRender[index] += '-'
            elif pin + prevPins == 10:
                frameRender[index] += '/'
            else:
                frameRender[index] += str(pin)
            if frameCounter < 10:
                    frameRender[index] += ' '
                    frameCounter += 1
            ballCounter = 0
            prevPins = 0

for game in frameRender:
    print(*game,sep='')
