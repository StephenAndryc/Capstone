"""
And so it begins....
"""
#external libraries
import random
import csv
#import json
#import numpy as np
#import matplotlib.pyplot as plt

#for consistency in trials, definitely be careful later on
random.seed(397)

#player objects
class player:
    def __init__ (self, name, profileArray):
        self.name = name #name to keep track of different players
        self.profileArray = profileArray #array that will encode decision-making rules
        self.money = 1500 #cash allotment at start of the game
        self.properties = [] #list of properties owned by player
        self.doubleRolls = 0 #number of consecutive double rolls by player (three sends to jail)
        self.communityChestJailFree = None #possesses community chest GOOJF card
        self.chanceJailFree = None #possesses chance GOOJF card
        self.position = 0 #location on the board
        self.alive = True #boolean for whether player is alive (if not skip on turns)

    def introduce (self):
        print(self.name)

#board object
class board:
    def __init__ (self):
        self.players = []
        self.squares = squaresArray()
    
    def addPlayer (self, newPlayer):
        self.players.append(newPlayer)
    
    def listPlayers (self):
        for people in self.players:
            people.introduce()

#general class for squares you can land on
class square:
    def __init__ (self, name, index):
        self.name = name
        self.index = index
        self.occupants = []
        # https://www.w3schools.com/python/python_inheritance.asp

class realEstate (square):
    def __init__ (self, name, index, price, aloneRent, setRent, oneRent, twoRent, threeRent, fourRent, hotelRent, houseCost, hotelCost, mortgageReturn, unmortgageCost):
        super().__init__(name, index)
        self.price = price
        self.aloneRent = aloneRent
        self.setRent = setRent
        self.oneRent = oneRent
        self.twoRent = twoRent
        self.threeRent = threeRent
        self.fourRent = fourRent
        self.hotelRent = hotelRent
        self.houseCost = houseCost
        self.hotelCost = hotelCost
        self.mortgageReturn = mortgageReturn
        self.unmortgageCost = unmortgageCost
        self.mortgaged = False
        self.owner = None

class railroad (square):
    def __init__ (self, name, index, price, oneRailroadRent, twoRailroadRent, threeRailroadRent, fourRailroadRent, mortgageReturn, unmortgageCost):
        super().__init__(name, index)
        self.price = price
        self.oneRailroadRent = oneRailroadRent
        self.twoRailroadRent = twoRailroadRent
        self.threeRailroadRent = threeRailroadRent
        self.fourRailroadRent = fourRailroadRent
        self.mortgageReturn = mortgageReturn
        self.unmortgageCost = unmortgageCost
        self.mortgaged = False
        self.owner = None

class utility (square):
    def __init__ (self, name, index, price, oneUtilityMultiplier, twoUtilityMultiplier, mortgageReturn, unmortgageCost):
        super().__init__(name, index)
        self.price = price
        self.oneUtilityMultiplier = oneUtilityMultiplier
        self.twoUtilityMultiplier = twoUtilityMultiplier
        self.mortgageReturn = mortgageReturn
        self.unmortgageCost = unmortgageCost
        self.mortgaged = False
        self.owner = None
        

def roll ():
    return random.randint(1,6) + random.randint(1,6)

#method that generates the list of property objects from a CSV file
def squaresArray ():
    squares_file = open("squares.csv")
    csv_reader = csv.reader(squares_file)
    rows = []
    index = 0
    for csv_row in csv_reader:
        if csv_row[1] == 'real estate':
            newRealEstate = realEstate(csv_row[0], index, int(csv_row[2]), int(csv_row[3]), int(csv_row[4]), int(csv_row[5]), int(csv_row[6]), int(csv_row[7]), int(csv_row[8]), int(csv_row[9]), int(csv_row[10]), int(csv_row[11]), int(csv_row[18]), int(csv_row[19]))
            rows.append(newRealEstate)
            index += 1
        elif csv_row[1] == 'railroad':
            newRailroad = railroad(csv_row[0], index, int(csv_row[2]), int(csv_row[12]), int(csv_row[13]), int(csv_row[14]), int(csv_row[15]), int(csv_row[18]), int(csv_row[19]))
            rows.append(newRailroad)
            index += 1
        elif csv_row[1] == 'utility':
            newUtility = utility(csv_row[0], index, int(csv_row[2]), int(csv_row[16]), int(csv_row[17]), int(csv_row[18]), int(csv_row[19]))
            rows.append(newUtility)
            index += 1
        elif csv_row[1] == 'other':
            newSquare = square(csv_row[0], index)
            rows.append(newSquare)
            index += 1
        else:
            1+1 #skips header row
            print(csv_row)
    squares_file.close()
    return rows

myArr = squaresArray()
for row in myArr:
    print(row.index, "-->", row.name, "type", type(row))

"""
#tests that roll empirical distribution mathces expectation
trials = []
for i in range(0,36000):
    trials.append(roll())

print(trials)
plt.hist(trials, bins = range(1,14))
plt.show()
"""