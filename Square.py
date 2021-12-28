#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script is designed to simulate the squares on the borad
"""

import csv


class Square:
    def __init__(self, name, index):
        self.name = name
        self.index = index
        self.occupants = []
        # https://www.w3schools.com/python/python_inheritance.asp


class RealEstate(Square):
    def __init__(self, name, index, price, aloneRent, setRent, oneRent,
                 twoRent, threeRent, fourRent, hotelRent, houseCost,
                 hotelCost, mortgageReturn, unmortgageCost):
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


class Railroad(Square):
    def __init__(self, name, index, price, oneRailroadRent, twoRailroadRent,
                 threeRailroadRent, fourRailroadRent, mortgageReturn,
                 unmortgageCost):
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


class Utility(Square):
    def __init__(self, name, index, price, oneUtilityMultiplier,
                 twoUtilityMultiplier, mortgageReturn, unmortgageCost):
        super().__init__(name, index)
        self.price = price
        self.oneUtilityMultiplier = oneUtilityMultiplier
        self.twoUtilityMultiplier = twoUtilityMultiplier
        self.mortgageReturn = mortgageReturn
        self.unmortgageCost = unmortgageCost
        self.mortgaged = False
        self.owner = None


class ToJail(Square):
    def intro(self):
        print("Go to jail directly, do not pass GO")


class card_deck:
    def __init__(self, name):
        self.name = name


class Community_chest(card_deck):
    def __init__(self, name):
        super().__init__(name)
        cards = {}
        cards[1] = "Advance to Go (Collect $200)"
        cards[2] = "Bank error in your favor. Collect $200"
        cards[3] = "Doctor’s fee. Pay $50"
        cards[4] = "From sale of stock you get $50"
        cards[5] = "Get Out of Jail Free"
        cards[6] = "Go to Jail. Go directly to jail, do not pass Go"
        cards[7] = "Holiday fund matures. Receive $100"
        cards[8] = "Income tax refund. Collect $20"
        cards[9] = "It is your birthday. Collect $10 from every player"
        cards[10] = "Life insurance matures. Collect $100"
        cards[11] = "Pay hospital fees of $100"
        cards[12] = "Pay school fees of $50"
        cards[13] = "Receive $25 consultancy fee"
        cards[14] = ("You are assessed for street repair."
                     + " 40 per house. $115 per hotel")
        cards[15] = "You have won second prize in a beauty contest.Collect $10"
        cards[16] = "You inherit $100"

        self.cards = cards

    def remove_jail_free(self):
        self.cards.pop(5)

    def add_jail_free(self):
        if 5 in self.cards:
            print("Card already in the deck, check your code!")
        else:
            self.cards[5] = "Get Out of Jail Free"


class Chance(card_deck):  # define the chance deck
    def __init__(self, name):
        super().__init__(name)
        cards = {}
        cards[1] = "Advance to Boardwalk"
        cards[2] = "Advance to Go (Collect $200)"
        cards[3] = "Advance to Illinois Avenue. If you pass Go, collect $200"
        cards[4] = "Advance to St. Charles Place. If you pass Go, collect $200"
        cards[5] = ("Advance to the nearest Railroad."
                    + "If unowned, you may buy it from the Bank."
                    + " If owned, pay wonder twice the rental to which they"
                    + " are otherwise entitled")
        cards[6] = ("Advance to the nearest Railroad. If unowned, you may buy"
                    + "it from the Bank. If owned, pay wonder twice the rental"
                    + " to which they are otherwise entitled")
        cards[7] = ("Advance token to nearest Utility. If unowned, you may buy"
                    + " it from the Bank. If owned, throw dice and pay owner a"
                    + " total ten times amount thrown")
        cards[8] = "Bank pays you dividend of $50"
        cards[9] = "Get Out of Jail Free"
        cards[10] = "Go Back 3 Spaces"
        cards[11] = "Go to Jail. Go directly to Jail, do not pass Go"
        cards[12] = ("Make general repairs on all your property."
                     + "For each house pay $25. For each hotel pay $100")
        cards[13] = "Speeding fine $15"
        cards[14] = ("Take a trip to Reading Railroad."
                     + "If you pass Go, collect $200")
        cards[15] = ("You have been elected Chairman of the Board."
                     + "Pay each player $50")
        cards[16] = "Your building loan matures. Collect $150"
        self.cards = cards

    def remove_jail_free(self):
        self.cards = self.cards.pop(9)

    def add_jail_free(self):
        if 9 in self.cards:
            print("Card already in the deck, check your code!")
        else:
            self.cards[9] = "Get Out of Jail Free"


# method that generates the list of property objects from a CSV file
def squaresArray():
    squares_file = open("squares.csv")
    csv_reader = csv.reader(squares_file)
    rows = []
    index = 0

    # instantiate the community chest deck
    community_chest_deck = Community_chest("community chest")

    # instantiate the chance deck
    chance_deck = Chance("chance")
    for csv_row in csv_reader:
        if csv_row[1] == 'real estate':
            newRealEstate = RealEstate(csv_row[0], index, int(csv_row[2]),
                                       int(csv_row[3]), int(csv_row[4]),
                                       int(csv_row[5]), int(csv_row[6]),
                                       int(csv_row[7]), int(csv_row[8]),
                                       int(csv_row[9]), int(csv_row[10]),
                                       int(csv_row[11]), int(csv_row[18]),
                                       int(csv_row[19]))
            rows.append(newRealEstate)
            index += 1
        elif csv_row[1] == 'railroad':
            newRailroad = Railroad(csv_row[0], index, int(csv_row[2]),
                                   int(csv_row[12]), int(csv_row[13]),
                                   int(csv_row[14]), int(csv_row[15]),
                                   int(csv_row[18]), int(csv_row[19]))
            rows.append(newRailroad)
            index += 1
        elif csv_row[1] == 'utility':
            newUtility = Utility(csv_row[0], index, int(csv_row[2]),
                                 int(csv_row[16]), int(csv_row[17]),
                                 int(csv_row[18]), int(csv_row[19]))
            rows.append(newUtility)
            index += 1
        elif csv_row[1] == 'other':
            newSquare = Square(csv_row[0], index)
            rows.append(newSquare)
            index += 1

        elif csv_row[1] == 'community chest':
            newSquare = Square(csv_row[0], index)
            newSquare.community_chest_deck = community_chest_deck
            rows.append(newSquare)
            index += 1

        elif csv_row[1] == 'chance':
            newSquare = Square(csv_row[0], index)
            newSquare.chance_deck = chance_deck
            rows.append(newSquare)
            index += 1

        elif csv_row[1] == "go to jail":
            newToJail = ToJail(csv_row[0], index)
            rows.append(newToJail)
            index += 1
        else:
            1+1  # skips header row
            # print(csv_row)
    squares_file.close()
    return rows


if __name__ == "__main__":
    board_array = squaresArray()
