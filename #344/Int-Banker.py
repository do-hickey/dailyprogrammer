"""This module solves the banker's algorithm.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #344 [Intermediate] Banker's Algorithm
https://www.reddit.com/r/dailyprogrammer/comments/7jkfu5/20171213_challenge_344_intermediate_bankers/

Submitted 1/26/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import re

def main():
    inputString = '''\
    [3 3 2]
    [0 1 0 7 5 3]
    [2 0 0 3 2 2]
    [3 0 2 9 0 2]
    [2 1 1 2 2 2]
    [0 0 2 4 3 3]'''

    impossibleInput = '''\
    [3 3 2]
    [0 1 0 7 6 3]
    [2 0 0 3 2 2]
    [3 0 2 11 0 2]
    [2 1 1 2 2 2]
    [0 0 2 4 3 3]'''

    #Note, switch the comment from the second to the first to enable the "impossible" scenario, in which:
    #P0 requires 6 of resource B and P2 requires 11 of resource A, both of which are not possible.
    inputLists = [re.findall(r'\d+',x) for x in inputString.split('\n')]
    #inputLists = [re.findall(r'\d+',x) for x in impossibleInput.split('\n')]

    currentRes = [int(item) for item in inputLists[0]]
    numRes = len(currentRes)
    allocRes = [[int(item) for item in row[0:numRes]] for row in inputLists[1:]]
    maxRes= [[int(item) for item in row[numRes:]] for row in inputLists[1:]]

    #Bonus code: First determine total resource of each type in the system
    totalResInSystem = [[sum(res) for res in zip(*allocRes)][res] + currentRes[res] for res in range(numRes)]

    completedProc = []
    impossibleProc = []
    while sum([sum(x) for x in allocRes]) > 0:
        for proc in range(len(inputLists)-1):
            resAreAvail = [allocRes[proc][res] + currentRes[res] >= maxRes[proc][res] for res in range(numRes)]
            if all(resAreAvail) and sum(allocRes[proc]) != 0:
                completedProc.append('P'+str(proc))
                currentRes = [currentRes[res] + allocRes[proc][res] for res in range(numRes)]
                allocRes[proc] = [0 for x in allocRes[proc]]
            #Bonus code to check if it can be completed at all, then release resources
            elif any([maxRes[proc][res] > totalResInSystem[res] for res in range(numRes)]):
                impossibleProc.append('P'+str(proc))
                currentRes = [currentRes[res] + allocRes[proc][res] for res in range(numRes)]
                allocRes[proc] = [0 for x in allocRes[proc]]
                maxRes[proc] = [0 for x in maxRes[proc]]

    if impossibleProc:
        print(f'Some processes are not possible: {impossibleProc}\nTheir resources were dumped to the pool for other processes.')
    print(f'Order of completed processes: {completedProc}')



if __name__ == '__main__':
    main()
