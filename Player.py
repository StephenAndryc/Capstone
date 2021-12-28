#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16

@author: sw

This script is designed to simulate players in the Monopoly game
"""

import numpy as np


class Player:
    def __init__(self, name, p_id, profileArray):
        self.name = name  # name to keep track of different players
        self.id = p_id
        self.alive = True  # boolean for whether player is alive
        self.active = False  # boolean that indicate if this is your turn
        self.dice1 = 0
        self.dice2 = 0
        self.position = 0  # location on the board
        self.money = 1500  # cash allotment at start of the game
        self.properties = []  # list of properties owned by player
        self.doubleRolls = 0  # number of consecutive double rolls
        self.communityChestJailFree = False  # possesses community chest GOOJF
        self.chanceJailFree = False  # possesses chance GOOJF card
        self.in_jail = 0

        self.profileArray = profileArray  # decision-making rules

    def start_turn(self):
        self.dice1 = 0
        self.dice2 = 0
        self.doubleRolls = 0
        self.active = True

    def introduce(self):
        print(self.name)

    def roll(self):
        if self.active:
            self.dice1 = np.random.choice(np.array([1, 2, 3, 4, 5, 6]))
            self. dice2 = np.random.choice(np.array([1, 2, 3, 4, 5, 6]))
            print(f"the two dices are {self.dice1} and {self.dice2}")

            if self.dice1 == self.dice2:
                self.doubleRolls += 1
                print("double Roll~!")
        else:
            print("not your turn, cannot do this")

    def move(self):
        if self.active:
            move = self.dice1 + self.dice2
            new_position = self.position + move
            self.position = new_position % 40
            print(f"move {move} steps, current position is {self.position}")
        else:
            print("not your turn, cannot do this")

    def draw_card(self, deck):

        def take_action(card_num, deck):
            deck_type = deck.name
            if deck_type == "community chest":
                print("draw from community chest and take the action")

                if card_num == 1:
                    pass
                elif card_num == 2:
                    pass
                elif card_num == 3:
                    pass
                elif card_num == 4:
                    pass
                elif card_num == 5:
                    self.communityChestJailFree = True
                    deck.remove_jail_free()
                elif card_num == 6:
                    self.position = 10
                    self.in_jail += 1
                elif card_num == 7:
                    pass
                elif card_num == 8:
                    pass
                elif card_num == 9:
                    pass
                elif card_num == 10:
                    pass
                elif card_num == 11:
                    pass
                elif card_num == 12:
                    pass
                elif card_num == 13:
                    pass
                elif card_num == 14:
                    pass
                elif card_num == 15:
                    pass
                elif card_num == 16:
                    pass
            if deck_type == "chance":
                print("draw from chance and take the action")

                if card_num == 1:  # advance to Boardwalk
                    self.position = 39
                elif card_num == 2:  # advance to GO
                    self.position = 0
                    self.money += 200
                elif card_num == 3:  # advance to Illinois Avenue
                    if self.position - 24 > 0:
                        self.position = 24
                        self.money += 200
                    else:
                        self.position = 24

                elif card_num == 4:  # advance to St. Charlet Place
                    if self.position - 11 > 0:
                        self.position = 11
                        self.money += 200
                    else:
                        self.position = 11

                elif card_num == 5:  # advance to nearest rail road
                    if self.position == 7:
                        self.position = 15
                    elif self.position == 22:
                        self.position = 25
                    elif self.position == 36:
                        self.position = 5

                elif card_num == 6:  # advance to nearest rail road
                    if self.position == 7:
                        self.position = 15
                    elif self.position == 22:
                        self.position = 25
                    elif self.position == 36:
                        self.position = 5
                    else:
                        print("something is wrong")

                elif card_num == 7:   # advance to nearest Utility
                    if self.position == 7:
                        self.position = 12
                    elif self.position == 22:
                        self.position = 28
                    elif self.position == 36:
                        self.position = 12
                    else:
                        print("something is wrong")

                elif card_num == 8:
                    pass
                elif card_num == 9:
                    self.chanceChestJailFree = True
                    deck.remove_jail_free()
                elif card_num == 10:
                    self.position -= 3

                elif card_num == 11:
                    print("go to jail")
                    self.position = 10
                    self.in_jail = 1

                elif card_num == 12:
                    pass
                elif card_num == 13:
                    pass
                elif card_num == 14:
                    if self.position - 5 > 0:
                        self.money += 200
                        self.position = 5
                    else:
                        self.position = 5
                elif card_num == 15:
                    pass
                elif card_num == 16:
                    pass

        card_dict = deck.cards  # load the given deck
        card_num = np.random.choice(list(card_dict))  # draw a card
        take_action(card_num, deck)  # take actions based on the draw
        print(f"the {card_num}th card from the {deck.name}")

    def buy_land(self):
        pass

    def buy_house(self):
        pass

    def sell_house(self):
        pass

    def trade(self):
        pass

    def counter_offer(self):
        pass

    def mortgage(self):
        pass

    def bail_out(self):
        if self.in_jail > 0:
            if self.money >= 50:
                self.money -= 50
                self.in_jail = 0
                print("bail your self out")
            else:
                print("don't have enough money to bail out")
        else:
            print("You are not in jail, no need for this!")

    def use_community_jail_card(self, community_chest_deck):
        if self.in_jail > 0 and self.active:
            if self.communityChestJailFree:
                print("use the card from community chest")
                self.communityChestJailFree = False
                self.in_jail = 0
                community_chest_deck.add_jail_free()  # return the card
            else:
                print("No jail free card from community chest")
        else:
            print("You are not in prison, can't use it")

    def use_chance_jail_card(self, chance_deck):
        if self.in_jail > 0 and self.active:
            if self.chanceJailFree:
                print("use the card from chance deck")
                self.chanceJailFree = False
                self.in_jail = 0
                chance_deck.add_jail_free()  # return the card
            else:
                print("No jail free card from the chance deck")

    def place_holder_move(self):
        pass

    def end_turn(self):
        self.active = False

    def reset_player(self):
        self.alive = True
        self.active = False
        self.position = 0
        self.money = 1500
        self.properties = []  # list of properties owned by player
        self.doubleRolls = 0  # number of consecutive double rolls
        self.communityChestJailFree = None  # possesses community chest GOOJF
        self.chanceJailFree = None  # possesses chance GOOJF card
        self.in_jail = 0


if __name__ == "__main__":
    agent1 = Player("steve", 0, None)
    agent1.roll_move()
    agent1.position
