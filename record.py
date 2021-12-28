#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18

@author: sw
"""


class Record_keeping():

    def __init__(self, player_dict):
        self.current_turn = 0
        self.total_players = 0
        self.player_dict = player_dict
        self.record_dict = None

