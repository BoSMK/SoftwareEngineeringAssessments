"""
@author: Bo Kaung
Utility Functions:
    createDeck
    swapPositions
    replaceAJQK
    suitDiff
    calcDistance
"""
import math
import itertools
import random


# set up Ranks and Suits
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
SUITS = ["C", "D", "H", "S"]


# Create a deck of cards
def createDeck():
    deck = ["".join(card) for card in itertools.product(RANKS, SUITS)]
    deck = list(deck)
    return deck


# Swap function to swap elements at given positions
    
def swapPositions(list, pos1, pos2): 
  
    # Storing the two elements 
    # as a pair in a tuple variable get 
    get = list[pos1], list[pos2] 
       
    # unpacking those elements 
    list[pos2], list[pos1] = get 
       
    return list


#+
# This function replaceAJQK:
# replace Ace with 1
# replace J, Q, K with 10
#-


def replaceAJQK(inputData):
    for i, r in enumerate(inputData): 
        if r[0] == 'A': inputData[i] = '1' + r[1]
        newListJ = inputData
        if r[0] == 'J': newListJ[i] = '10'+ r[1]
        newListQ = newListJ
        if r[0] == 'Q': newListQ[i] = '10'+ r[1]
        newListK = newListQ      
        if r[0] == 'K': newListK[i] = '10'+ r[1]
        newListAJQK = newListK
        
    return newListAJQK

#print("New test ", replaceAJQKHDCS(json_file))

          
'''
1. the difference of the ranks of the two entries, when the entries share the same suit; otherwise	
2. twice the difference of the ranks of the two entries, when the entries share the same color; otherwise	
3. three times the difference of the ranks of the two entries, when the entries have different colors.	

# Distance (Waste Metric)   
D and D = 1 	   D and H = 2        D and C = 3
H and H = 1        S and C = 2	      D and S = 3
C and C = 1                           H and C = 3
S and S = 1                           H and S = 3
'''

def suitDiff(card1, card2):

    if (card1 == card2): 
        suitDiff = 1
        return suitDiff
    if (card1 == 'D' and card2 == 'H') or (card1 == 'H' and card2 == 'D') or \
        (card1 == 'S' and card2 == 'C') or (card1 == 'C' and card2 == 'S'): 
        suitDiff = 2 
        return suitDiff
    if (card1 == 'D' and card2 == 'C') or (card1 == 'C' and card2 == 'D') or \
        (card1 == 'D' and card2 == 'S') or (card1 == 'S' and card2 == 'D') or \
        (card1 == 'H' and card2 == 'C') or (card1 == 'C' and card2 == 'H') or \
        (card1 == 'H' and card2 == 'S') or (card1 == 'S' and card2 == 'H'):
        suitDiff = 3 
        return suitDiff

#+
# This function CaclDistance
# Calls function suitDiff to identify difference between two suits
# calculate absolute value between two suits
# return distance between two cards[] = absolute value of (current rank - next rank) x suitDiff
#-

def calcDistance(data):

    d = data
    distance = []
    for cur, nxt in zip(d, d[1:]):
        rankx = cur[-1]                
        ranky = nxt[-1]

        suitx = cur.strip(rankx)
        suity = nxt.strip(ranky)

        diffSuit = suitDiff(rankx, ranky)
        #print("Difference : ", diffSuit)
        
        #The distance between two successive entries is the absolute value of:
        res  = abs(int(suitx) - int(suity)) * diffSuit            
        #print("Res : ", res)
        distance.append(res)
        #print("Distance : ", distance)
            
    return distance
    
'''
def main():
    deck = Deck()
    print(deck)


if __name__ == "__main__":
    main()
'''
