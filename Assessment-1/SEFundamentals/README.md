### Programming language: Python 3.7.3
### OS - WINDOWS or LINUX

### Contain
```
1. utility.py
   Functions:
    	createDeck
	swapPositions
	replaceAJQK
	suitDiff
	calcDistance

2. is-invalid-batch.py
   Function : isValidBatch

3. waste-metric.py
   Function: wasteMetric

4. one-swap-recommendation.py
   Functions:
	oneSwap
	oneSwapRecommendation

5. two-swap-recommendation.py
   Functions:
	twoSwap
	twoSwapRecommendation   
```
### Usage

```
To determine whether Json file is a valid file or not!

python is-invalid-batch.py
Please enter file name : batch-xx.json
```

```
To calculate Waste Metric (sum of distances between cards)
python waste-metric.py
Please enter file name : batch-xx.json
```

### Two scenarios below may only works for Valid JSON files (Batch-00.json ... Batch-13.json)
```
Swap one time (two cards) and see Waste Metric
python one-swap-recommendation.py
Please enter file name : batch-xx.json
```

```
Swap two times (four cards) and see Waste Metric
python two-swap-recommendation.py
Please enter file name : batch-xx.json
```

