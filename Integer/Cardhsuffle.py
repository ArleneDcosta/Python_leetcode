# Python3 implementation of the approach

# Total cards
CARDS = 100;

# Function to perform the current round
def currentRound(list1, totalPiles):

	# Create the required empty piles
	piles = [];
	for i in range(totalPiles):
		piles.append([])

		# Add cards to the piles one by one
	j = 0;
	for i in range(CARDS):
		piles[j].append(list1[i])
		j = (j + 1) % totalPiles
	
	# After all the piles have been reversed
	# the new order will be first card of the
	# first pile, second card of the first
	# pile, ..., last pile of the last pile
	# (from top to bottom)
	pileNo = 0
	i = 0
	j = 0
	while (i < CARDS):
		list1.insert(i, piles[pileNo][j])
		j += 1
		if (j >= len(piles[pileNo])):
			pileNo += 1
			j = 0
		
		i += 1
	
# Function to perform all the rounds
def performRounds(rounds,piles, n):

	# Create the initial list1 with all the cards
	list1 = [];
	for i in range(1, CARDS + 1):
		list1.append(i);

	# Perform all the rounds
	for i in range(rounds):
		currentRound(list1, piles[i]);

	# Return the nth card
	return list1[n];



#rounds = len(piles)
print(performRounds(2,[2,2],4))
