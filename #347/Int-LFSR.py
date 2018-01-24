"""This module implements a Linear Feedback Shift Register.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #347 [Intermediate] Linear Feedback Shift Register
https://www.reddit.com/r/dailyprogrammer/comments/7r17qr/20180117_challenge_347_intermediate_linear/?st=jcrv9jgq&sh=b641238e

Submitted 1/22/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import re
def feedback(bitA, bitB, feedFunc):
    if feedFunc == 'XOR':
        return bool(bitA) ^ bool(bitB)
    else:
        return not (bool(bitA) ^ bool(bitB))

while True:
    expression = input("LFSR Input: ")
    if re.match(r'\[(\d+,)+\d+\]\sXN?OR\s[0,1]+\s[1-9]\d*',expression):
        break

origTapPos = eval(re.search(r'^\[(\d|,)+\]',expression).group(0))
feedFunc = re.search(r'XN?OR',expression).group(0)
bitString = re.search(r'\s\d+\s',expression).group(0).strip()
iterCount = int(re.search(r'\s\d+$',expression).group(0).strip())

print(f'0 {bitString}')
for iterant in range(1, iterCount+1):
    tapPos = origTapPos
    bitOne = int(bitString[tapPos[-1]])
    bitTwo = int(bitString[tapPos[-2]])
    newBit = int(feedback(bitOne, bitTwo, feedFunc))
    tapPos = tapPos[0:-2]

    while len(tapPos) > 0:
        bitThree = int(bitString[tapPos[-1]])
        newBit = int(feedback(newBit, bitThree, feedFunc))
        del tapPos[-1]

    bitString = str(newBit) + bitString[0:-1]
    print(f'{iterant} {bitString}')



