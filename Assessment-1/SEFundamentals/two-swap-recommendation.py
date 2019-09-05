# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:23:50 2019
@author: bo

Functions:
twoSwap
twoSwapRecommendation
"""

import json
import numpy as np
import collections
from utility import calcDistance, replaceAJQK, swapPositions


#+
# Function twoSwap
# 2 swaps of 4 entries from the list
#-


def twoSwap(data):
    d = data
    pos1 = 1
    pos2 = 51
    pos3 = 0
    pos4 = 27
    oneSwapData = swapPositions(d,pos1, pos2)
    #print("OneSwap : ", oneSwapData)
    twoSwapData = swapPositions(oneSwapData,pos3, pos4)
    #print("twoSwap : ", twoSwapData)
    return twoSwapData


#+        
# twoSwapRecommendation function
# Take input json file
# function replaceAJQK will replace those values
# function calDistance to calculate Waste Metric
# function twoSwap to swap four entries
#-


def twoSwapRecommendation(json_file):

    file = open(json_file)
    with file as json_data:
        d = json.load(json_data)
        #Total_cards = len(d)
    
    # debug to see Json file has 52 entries
    #print("total: ", Total_cards)    
    input_arr = d

    res= replaceAJQK(input_arr)
    a = calcDistance(res)
    wasteMetric = sum(a)
    print("Waste Metric : ", wasteMetric)

    #Two Swap
    SwapData = twoSwap(res)
    CalcSwapData = calcDistance(SwapData)
    twoSwapMetric = sum(CalcSwapData)
    print("Waste Metric After Two Swap : ", twoSwapMetric)
    

# Provide input Json file name
json_file = input("Please enter file name : ")
twoSwapRecommendation(json_file)
