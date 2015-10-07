""" A recursive dynamic programming solution to change making."""
coins = (1,3,4,7)
total = 27
dict={}


def minCoins(total, coins):
	if str(total) in dict:
		return dict[str(total)]	elif total in coins:
		return 1
	else:
		possSol=[]#list of possible solutions
		for i in coins:
			if total-i > 0: #makes sure no negative numbers are returned
				possSol.append(minCoins(total-i, coins)+1)#recursive call, 
		dict[str(total)] = min(possSol)
		return min(possSol)




print minCoins(total, coins)
for key,values in dict.items():
	print key, ":", values