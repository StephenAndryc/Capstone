#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18

@author: sw
"""

from Player import Player
from Square import squaresArray
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# print(player1.__dict__)

# player1.reset_player()

record_keeping = {}

# 1. prepare the game

# 1.1 instantiate the players
player1 = Player("p1", 0, None)
player2 = Player("p2", 0, None)

# 1.2 instantiate the board, specify special positions
board_array = squaresArray()
community_chest_position = [2, 27, 33]
chance_position = [7, 22, 36]

# 1.3 prepare the community chest deck
community_chest_deck = board_array[2].community_chest_deck

# 1.4 prepare the chance deck
chance_deck = board_array[7].chance_deck


# let one player move for x turns
t = 0
while t <= 3000:
    player1.start_turn()  # turn active to True
    print(f"now playing round {t}")

    # phase 1. check jail status and take certain action
    while player1.in_jail > 0 and player1.in_jail <= 3:
        print(f"the {player1.in_jail} turns in jail")
        # if have a jail free card, always use it
        # if no card, roll the dice (i.e. no bail out option)
        # or stay longer than 3 turns
        # no bail out option for now : player1.bail_out()
        player1.use_community_jail_card(community_chest_deck)
        if player1.in_jail == 0:
            break
        else:
            player1.use_chance_jail_card(chance_deck)
            if player1.in_jail == 0:
                break
            else:
                player1.roll()
                if player1.dice1 == player1.dice2:
                    print("double! out of jail!")
                    player1.in_jail = 0
                    player1.doubleRolls = 0
                    player1.move()
                    player1.place_holder_move()  # trade, buy, sell, etc
                    player1.end_turn()  # skip the regular move phase
                    break
                else:
                    print("no luck, stay in jail")
                    player1.in_jail += 1
                    player1.end_turn()
                    break

    # phase 2. take actions
    while player1.active:

        # regular roll & move
        if player1.in_jail == 4:  # if you spent 3 turns in jail
            print("already three turns in jail, get out and move")
            player1.in_jail = 0

        while player1.doubleRolls < 3:
            player1.roll()  # roll the dice
            player1.move()  # move forward
            player1.place_holder_move()  # you can do something
            if player1.position == 30:
                print("go to jail")
                player1.position = 10
                player1.in_jail = 1
                player1.doubleRolls = 0
                player1.place_holder_move()  # can do sth
                player1.end_turn()  # end your turn
                break
            elif player1.position in community_chest_position:
                player1.draw_card(community_chest_deck)
                player1.place_holder_move()  # can do sth
            elif player1.position in chance_position:
                player1.draw_card(chance_deck)
                player1.place_holder_move()  # can do sth
            else:
                player1.place_holder_move()

            if player1.dice1 == player1.dice2:
                continue
            else:
                player1.end_turn()  # end your turn
                break

        if player1.doubleRolls == 3:
            print("three doubles in a row, go to jail")
            player1.position = 10
            player1.in_jail += 1
            player1.end_turn()  # end your turn

    print("=======================")
    # record keeping track positions
    record_keeping[t] = player1.position
    t += 1


record = list(record_keeping.values())
record.sort()

record = np.array(record)
plt.hist(record, bins=40, density=True, edgecolor='black')

prob_table = {}
for i in range(0, 40):
    prob_table[i] = np.count_nonzero(record == i)/3000

prob_table = pd.DataFrame.from_dict(prob_table, orient="index",
                                    columns=['prob'])

prob_table.to_csv("prob_table.csv")

"""
rail road prob
rr1 = np.count_nonzero(record == 5)
rr2 = np.count_nonzero(record == 15)
rr3 = np.count_nonzero(record == 25)
rr4 = np.count_nonzero(record == 35)
rr_cost = 200 + 200 + 50 + 50
rr_prob = (rr1 + rr2 + rr3 + rr4)/3001
rr_cost/(rr_prob*200)


sq_prob = np.count_nonzero(record == 28)/3001
"""
