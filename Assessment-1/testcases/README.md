This assessment includes: Software Engineering Fundamentals

    is-invalid-batch JSON-FILE
    waste-metric JSON-FILE
    one-swap-recommendation JSON-FILE
    two-swap-recommendation JSON-FILE

///////////////////////////////////////////////////////////////////////////////////////////

Programming language: Python 3.7.3

1. utility.py
2. is-invalid-batch.py
3. waste-metric.py
4. one-swap-recommendation.py
5. two-swap-recommendation.py

///////////////////////////////////////////////////////////////////////////////////////////

file name : utility.py
Utility Functions:
    createDeck
    swapPositions
    replaceAJQK
    suitDiff
    calcDistance
	
///////////////////////////////////////////////////////////////////////////////////////////

is-invalid-batch JSON-FILE
file name : is-invalid-batch.py
Function : isValidBatch

i.e.
C:\Projects\GitHub\kaung-bo-20190725>python is-invalid-batch.py
Please enter file name : batch-00.json
total:  52
input :  ['10C' '10D' '10H' '10S' '2C' '2D' '2H' '2S' '3C' '3D' '3H' '3S' '4C' '4D'
 '4H' '4S' '5C' '5D' '5H' '5S' '6C' '6D' '6H' '6S' '7C' '7D' '7H' '7S'
 '8C' '8D' '8H' '8S' '9C' '9D' '9H' '9S' 'AC' 'AD' 'AH' 'AS' 'JC' 'JD'
 'JH' 'JS' 'KC' 'KD' 'KH' 'KS' 'QC' 'QD' 'QH' 'QS']
Cards ok? : True
It is a valid batch file.

python is-invalid-batch.py
Please enter file name : batch-15.json
total:  52
input :  ['10C' '10D' '10H' '10S' '2C' '2D' '2H' '2S' '3C' '3D' '3H' '3S' '4C' '4D'
 '4H' '4T' '5C' '5D' '5H' '5S' '6C' '6D' '6H' '6S' '7C' '7D' '7H' '7S'
 '8C' '8D' '8H' '8S' '9C' '9D' '9H' '9S' 'AC' 'AD' 'AH' 'AS' 'JC' 'JD'
 'JH' 'JS' 'KC' 'KD' 'KH' 'KS' 'QC' 'QD' 'QH' 'QS']
Cards ok? : False
It is not a valid batch file.

///////////////////////////////////////////////////////////////////////////////////////////

waste-metric JSON-FILE
file name: waste-metric.py
Function: wasteMetric
i.e
python waste-metric.py
Please enter file name : batch-00.json
Waste Metic is :  335

///////////////////////////////////////////////////////////////////////////////////////////

one-swap-recommendation JSON-FILE
file name : one-swap-recommendation
Functions:
    oneSwap
    oneSwapRecommendation

python one-swap-recommendation.py
Please enter file name : batch-xx.json

///////////////////////////////////////////////////////////////////////////////////////////

two-swap-recommendation JSON-FILE
file name : two-swap-recommendation
Functions:
    twoSwap
    twoSwapRecommendation
python two-swap-recommendation.py
Please enter file name : batch-xx.json

///////////////////////////////////////////////////////////////////////////////////////////
