This exercise includes a deck of cards in a random order to represent a process batch.
```
Each batch is represented as a json array consisting of 52 entries. Each such entry is a string where 
the initial characters are one of 
{"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"} 
and the final character is one of the characters in "CHSD".

Similar to a shuffled deck of cards, a valid batch consists of each of the possible 
52 entries in a specified order.

For example, ../testcases/batch-00.json represents a valid batch.
Each entry has a rank, a suit, and a color:
	• The rank of each entry is determined by its initial character(s), 
	where: the rank of "A" equals 1; the rank of "2" through "9" equals the corresponding integer; 
	and the rank of "10", "J", "Q", and "K" equals 10.
	• The suit of each entry is determined by its final character, where: the suit of "C" = Club; 
	the suit of "H" = Heart; the suit of "S" = Spade; and the suit of "D" = Diamond.
	• The color of each entry is determined by its suit, where: the color of Clubs and Spades is Black;
	and the color of Hearts and Diamonds is Red.

Rank: 
A = 1
2, 3, 4, 5, 6, 7, 8, 9
10, J, Q, K = 10

Suit:		Color
 "C" = Club 		(Black)
 "S" = Spade 			(Black)
 "D" = Diamond 			(Red)
 "H" = Heart 			(Red)

Customer subject matter experts have indicated that processing each batch entails a unitless waste metric. 
They suggest that waste for a batch can be estimated as the sum of the distances between successive entries 
within the batch, that is: between first and second entries, second and third entries, third and fourth entries, etc. 
The distance between two successive entries is the absolute value of:

	1. the difference of the ranks of the two entries, when the entries share the same suit; otherwise
	2. twice the difference of the ranks of the two entries, when the entries share the same color; otherwise
	3. three times the difference of the ranks of the two entries, when the entries have different colors.
	
Development Constraints
	1. Use whatever language you'd like that can build / deploy to a Linux environment. It should be able 
	to be invoked from the linux command line as specified in the user story, after we follow the instructions 
	that you provide in your deliverable's README.
	
User Story
As the customer I would like to be able to provide a JSON representation of a batch and:
	1. receive an alarm if the batch is invalid
	2. understand the waste metric for the batch
	3. receive a proactive recommendation that maximizes reduction in the waste metric if one swap of 
	any two entries anywhere in the batch could occur
	4. receive a proactive recommendation that maximizes reduction in the waste metric if two swaps of 
	any two entries anywhere in the batch could occur
```

