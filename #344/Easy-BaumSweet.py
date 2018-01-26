"""This module returns the Baum-Sweet Sequence for 0 to n, where n is the input from the user.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #344 [Easy] Baum-Sweet Sequence
https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/

Submitted 1/25/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

def main():
    n = int(input('Generate sequence from 0 to: '))
    result = [baumSweet2(n) for n in range(n+1)]
    print(result)

def baumSweet(x):
    numZeros = 0
    xBin = bin(x)[2:]

    if x == 0:
        return 1
    for index, i in enumerate(xBin):
        if i == '0':
            numZeros += 1
            if index == len(xBin) - 1 and numZeros % 2 == 1:
                return 0
        if i == '1':
            if numZeros % 2 == 1:
                return 0
            else:
                numZeros = 0
    return 1

def baumSweet2(n):
    '''See reddit discussion at link below for basis of this algorithm (changed slightly).
    https://www.reddit.com/r/dailyprogrammer/comments/7j33iv/20171211_challenge_344_easy_baumsweet_sequence/drfg6go/?st=jcvetqqx&sh=e46564d9'''
    hasOdds = len([n for n in filter(None, bin(n)[2:].split("1")) if len(n) % 2 != 0])
    if hasOdds and n != 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    main()
