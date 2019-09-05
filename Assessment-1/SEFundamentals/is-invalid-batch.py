"""
@author: Bo Kaung

This function :
    isValidBatch will verify data from input json file
"""

import json
import numpy as np
from utility import createDeck


#+
# This function isValidBatch
# input json file
# eveluate by counting the deck and compare with organic deck
#-
 

def isValidBatch(json_file):
    # load json file
    file = open(json_file)
    with file as json_data:
        d = json.load(json_data)
        Total_cards = len(d)

    # debug to see Json file has 52 entries
    print("total: ", Total_cards)
    input_arr = np.array(d)
    # Sort input file data
    input_cards = np.sort(input_arr)
    print("input : ", input_cards)

    # Sort original deck
    orig_deck = sorted(createDeck())

    # Compare input file vs original deck of cards
    res = np.array_equal(input_cards, orig_deck)  # test if same shape, same elements values

    print("Cards ok? :", res)

    # verify 52 cards in the file
    if Total_cards == 52 and res:
        valid_p = print("It is a valid batch file.")
    else:
        valid_p = print("It is not a valid batch file.")
    file.close()
    return valid_p


# Provide input Json file name
json_file = input("Please enter file name : ")
isValidBatch(json_file)