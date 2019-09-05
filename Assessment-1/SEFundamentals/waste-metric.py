# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:23:50 2019
@author: bo

Function:
    wasteMetric
"""


import json
import numpy as np
import collections
from utility import calcDistance, replaceAJQK


#+        
# wasteMetric function
# Take input json file
# function replaceAJQK will replace those values
# function calDistance to calculate Wast Metric
#-


def wasteMetric(json_file):

    file = open(json_file)
    with file as json_data:
        d = json.load(json_data)
        #Total_cards = len(d)
    
    # debug to see Json file has 52 entries
    #print("total: ", Total_cards)    
    input_arr = d

    res= replaceAJQK(input_arr)
    a = calcDistance(res)
    print("Waste Metic is : ", sum(a) )
    wasteMetric = sum(a)
    return wasteMetric


# Provide input Json file name
json_file = input("Please enter file name : ")
wasteMetric(json_file)