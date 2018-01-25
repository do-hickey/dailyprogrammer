"""This module solves cryptarithmetic problems.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #346 [Easy] Cryptarithmetic Solver
https://www.reddit.com/r/dailyprogrammer/comments/7p5p2o/20180108_challenge_346_easy_cryptarithmetic_solver/

Submitted 1/25/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

import itertools

def main():
    inputStrings = [
    "WHAT + WAS + THY == CAUSE",
    "HIS + HORSE + IS == SLAIN",
    "HERE + SHE == COMES",
    "FOR + LACK + OF == TREAD",
    "I + WILL + PAY + THE == THEFT",
    "TEN + HERONS + REST + NEAR + NORTH + SEA + SHORE + AS + TAN + TERNS + SOAR + TO + ENTER + THERE + AS + HERONS + NEST + ON + STONES + AT + SHORE + THREE + STARS + ARE + SEEN + TERN + SNORES + ARE + NEAR == SEVVOTH",
    "SO + MANY + MORE + MEN + SEEM + TO + SAY + THAT + THEY + MAY + SOON + TRY + TO + STAY + AT + HOME +  SO + AS + TO + SEE + OR + HEAR + THE + SAME + ONE + MAN + TRY + TO + MEET + THE + TEAM + ON + THE + MOON + AS + HE + HAS + AT + THE + OTHER + TEN == TESTS",
    "THIS + A + FIRE + THEREFORE + FOR + ALL + HISTORIES + I + TELL + A + TALE + THAT + FALSIFIES + ITS + TITLE + TIS + A + LIE + THE + TALE + OF + THE + LAST + FIRE + HORSES + LATE + AFTER + THE + FIRST + FATHERS + FORESEE + THE + HORRORS + THE + LAST + FREE + TROLL + TERRIFIES + THE + HORSES + OF + FIRE + THE + TROLL + RESTS + AT + THE + HOLE + OF + LOSSES + IT + IS + THERE + THAT + SHE + STORES + ROLES + OF + LEATHERS + AFTER + SHE + SATISFIES + HER + HATE + OFF + THOSE + FEARS + A + TASTE + RISES + AS + SHE + HEARS + THE + LEAST + FAR + HORSE + THOSE + FAST + HORSES + THAT + FIRST + HEAR + THE + TROLL + FLEE + OFF + TO + THE + FOREST + THE + HORSES + THAT + ALERTS + RAISE + THE + STARES + OF + THE + OTHERS + AS + THE + TROLL + ASSAILS + AT + THE + TOTAL + SHIFT + HER + TEETH + TEAR + HOOF + OFF + TORSO + AS + THE + LAST + HORSE + FORFEITS + ITS + LIFE + THE + FIRST + FATHERS + HEAR + OF + THE + HORRORS + THEIR + FEARS + THAT + THE + FIRES + FOR + THEIR + FEASTS + ARREST + AS + THE + FIRST + FATHERS + RESETTLE + THE + LAST + OF + THE + FIRE + HORSES + THE + LAST + TROLL + HARASSES + THE + FOREST + HEART + FREE + AT + LAST + OF + THE + LAST + TROLL + ALL + OFFER + THEIR + FIRE + HEAT + TO + THE + ASSISTERS + FAR + OFF + THE + TROLL + FASTS + ITS + LIFE + SHORTER + AS + STARS + RISE + THE + HORSES + REST + SAFE + AFTER + ALL + SHARE + HOT + FISH + AS + THEIR + AFFILIATES + TAILOR + A + ROOFS + FOR + THEIR + SAFE == FORTRESSES"
    ]

    #Handle strings - split into individual words, remove operators
    splitStrings = [line.split(' ') for line in inputStrings]
    for index,stringItem in enumerate(splitStrings):
        splitStrings[index] = [word for word in stringItem if (word != '+' and word != "==" and word != '')]

    solutionDicts = [{}]*len(splitStrings)
    for index in range(len(splitStrings)):
        solutionDicts[index] = cryptarithmeticSolver(splitStrings[index])
    for solution in solutionDicts:
        for key in sorted(solution):
            print(f'{key}=>{solution[key]}', end=' ')
        print("")

def cryptarithmeticSolver(equationWords):
    '''Returns the dictionary that solves addition-based cryptarithms provided as a list of strings with the resultant as the last word'''
    #assemble set of letters that cannot represent 0
    nonZeros = {word[0] for word in equationWords}

    #assemble all letters used in the puzzle (make it a set then convert back to list to remove duplicates.
    #order is unimportant, but must remain constant after the list is finished being created, hence not being left as a set.
    allLettersList = []
    for word in equationWords:
        allLettersList += list(word)
    allLettersList = list(set(allLettersList))

    letterDict = dict.fromkeys(allLettersList)
    numberIterator = itertools.permutations(range(10))

    while True:
        currentSum = 0
        #use the numberIterator to interate through all pemutations of 0-9, each time updating the dictionary and checking for the proper solution
        pairs = zip(allLettersList,next(numberIterator))
        for pair in pairs:
            if ((pair[0] in nonZeros) and (pair[1] == 0)): #check for non-allowed leading zeros
                break
            else:
                letterDict[pair[0]] = pair[1] #if allowed, update dictionary accordingly

        else: #will only execute if "for" loop above finished normally. If the "break" statement was hit, the next "while" will execute
            for word in equationWords[:-1]:
                currentSum += wordValue(word,letterDict)
            resultWordSum = wordValue(equationWords[-1],letterDict)

            if currentSum == resultWordSum:
                return letterDict


def wordValue(word,letterDict):
    '''Returns the value of a word given the word and a value dictionary'''
    wordVal = 0
    for index, letter in enumerate(word):
        wordVal += letterDict[letter]*pow(10,len(word)-1-index)

    return wordVal


if __name__ == '__main__':
    main()