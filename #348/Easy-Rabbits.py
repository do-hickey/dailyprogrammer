"""This module determines the timeline for rabbit domination.

Problem statement from www.reddit.com/r/dailyprogrammer.
Challenge #348 [Easy] The Rabbit Problem
https://www.reddit.com/r/dailyprogrammer/comments/7s888w/20180122_challenge_348_easy_the_rabbit_problem/?st=jcrvajuc&sh=acf0047f

Submitted 1/23/2018
"""

__version__ = '0.0'
__author__ = 'Ilan Cohn'

class Rabbit:
    numMales = 0
    numFemales = 0
    numDead = 0

    deadAge = 96
    fertileAge = 4
    infertileAge = 96

    litterMale = 5
    litterFemale = 9


    def __init__(self, currAge, gender, population):
        self.gender = gender
        self.population = population
        self.currAge = currAge

        if gender == "Male":
            Rabbit.numMales += population
        else:
            Rabbit.numFemales += population

    def age(self):
        if self.currAge == Rabbit.deadAge:
            Rabbit.numDead += self.population
            if self.gender == "Male":
                Rabbit.numMales -= self.population
            else:
                Rabbit.numFemales -= self.population

            self.population = 0
            return (0,0)

        elif self.gender == "Male":
            self.currAge += 1
            return (0,0)

        elif (self.currAge >= Rabbit.fertileAge) and (self.currAge < Rabbit.infertileAge):
            self.currAge += 1
            return (Rabbit.litterMale*self.population, Rabbit.litterFemale*self.population)

        else:
            self.currAge += 1
            return (0,0)

rabbitGens = []
currGen = 0
startingMales = 2
startingFemales = 4
totalNeeded = 1000000000

rabbitGens.insert(0,Rabbit(2,"Male",startingMales))
rabbitGens.insert(0,Rabbit(2,"Female",startingFemales))

while Rabbit.numMales + Rabbit.numFemales < totalNeeded:
#while Rabbit.numDead == 0:
    newMales = 0
    newFemales = 0

    for bunnies in rabbitGens:
        (addMales, addFemales) = bunnies.age()
        newMales += addMales
        newFemales += addFemales

    rabbitGens.insert(0,Rabbit(0,"Male",newMales))
    rabbitGens.insert(0,Rabbit(0,"Female",newFemales))
    currGen += 1

print(f'Months: {currGen}\nDead Bunnies: {Rabbit.numDead}')