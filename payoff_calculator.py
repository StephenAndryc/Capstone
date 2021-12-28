#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:50:09 2021

@author: sw
"""

# from Player import Player
from Square import squaresArray, RealEstate
import numpy as np
# import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 1.2 instantiate the board
board_array = squaresArray()

real_estate_revenue = {}
for square in board_array:
    if isinstance(square, RealEstate):
        real_estate_revenue[square.index] = [square.aloneRent, square.oneRent,
                                             square.twoRent, square.threeRent,
                                             square.fourRent, square.hotelRent]

real_estate_revenue = pd.DataFrame.from_dict(real_estate_revenue,
                                             orient="index",
                                             columns=["aloneRent", "oneRent",
                                                      "twoRent", "threeRent",
                                                      "fourRent", "hotelRent"])


real_estate_cost = {}
for square in board_array:
    if isinstance(square, RealEstate):
        real_estate_cost[square.index] = [square.price, square.houseCost,
                                          square.houseCost*2,
                                          square.houseCost*3,
                                          square.houseCost*4,
                                          square.houseCost*4
                                          + square.hotelCost]

real_estate_cost = pd.DataFrame.from_dict(real_estate_cost,
                                          orient="index",
                                          columns=["price", "oneCost",
                                                   "twoCost", "threeCost",
                                                   "fourCost", "hotelCost"])

prob_table = pd.read_csv("prob_table.csv", index_col=0)

real_estate_prob = prob_table[prob_table.index.isin(real_estate_revenue.index)]

real_estate_prob = np.repeat(np.array(real_estate_prob), 6, axis=1)

expected_payoff = real_estate_prob * real_estate_revenue

real_estate_breakeven = np.array(real_estate_cost)/expected_payoff


square_table = pd.read_csv("squares.csv")
square_table = square_table[["Square Name", "Category", "color", "position"]]
real_estate_name = square_table[square_table["Category"] == "real estate"]
real_estate_name = list(real_estate_name["Square Name"])

real_estate_breakeven.columns = ["PropertyOnly", "One House", "Two Houses",
                                 "Three Houses", "Four Houses", "Hotel"]

real_estate_breakeven.index = real_estate_name
real_estate_breakeven.to_csv("breakeven.csv")

sns.heatmap(pd.DataFrame(real_estate_breakeven), annot=True, cmap="YlGnBu")
