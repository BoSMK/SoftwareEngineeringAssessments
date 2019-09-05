# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:23:50 2019
@author: bo

Functions:
    oneSwap
    oneSwapRecommendation
"""


import json
import numpy as np
import collections
from utility import calcDistance, replaceAJQK, swapPositions


#+
# function OneSwap will do one swap of two entries
#-


def OneSwap(data):
    d = data
    pos1 = 10
    pos2 = 35
    newData = swapPositions(d,pos1, pos2)
    return newData
    
#print("New Data : ", OneSwap(data))


#+        
# oneSwapRecommendation function
# Take input json file
# function replaceAJQK will replace those values
# function calDistance to calculate Wast Metric
#-


def oneSwapRecommendation(json_file):

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
    print("Waste Metric ", wasteMetric)

    #OneSwap
    SwapData = OneSwap(res)
    CalcSwapData = calcDistance(SwapData)
    oneSwapMetric = sum(CalcSwapData)
    print("Waste Metric After One Swap : ", oneSwapMetric)
    

# Provide input Json file name
json_file = input("Please enter file name : ")
oneSwapRecommendation(json_file)
