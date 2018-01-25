"""This module uses Fermat's Little Theorem to check the primality of a number to a required certainty.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #346 [Intermediate] Fermat's little theorem
https://www.reddit.com/r/dailyprogrammer/comments/7pmt9c/20180110_challenge_346_intermediate_fermats/

Submitted 1/25/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import random

inputLines = '''\
29497513910652490397 0.9
29497513910652490399 0.9
95647806479275528135733781266203904794419584591201 0.99
95647806479275528135733781266203904794419563064407 0.99
2367495770217142995264827948666809233066409497699870112003149352380375124855230064891220101264893169 0.999
2367495770217142995264827948666809233066409497699870112003149352380375124855230068487109373226251983 0.999'''

inputListStr = [line.split(" ") for line in inputLines.split('\n')]
inputList = [[int(line[0]), float(line[1])] for line in inputListStr]

def fermatThrmFunc(inputPair):
    possPrime = inputPair[0]
    reqCertainty = inputPair[1]
    numsTested = 0

    while True:
        base = random.randint(1,possPrime-1)
        if pow(base,possPrime,possPrime) == base:
            numsTested += 1
            actCertainty = 1 - pow(0.5,numsTested)
            if actCertainty >= reqCertainty:
                print(True) #show result to console
                return True #for use if this is to be implemented where the return value is used
        else:
            print(False)
            return(False)

for inputPair in inputList:
    fermatThrmFunc(inputPair)