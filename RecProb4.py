"""
Again, using no loops, no global variables, and without asking for the length of the array except to check if it's empty, write a function that returns the last index of a given input in a list. Negative one gets returned if the element doesn't occur in the list. Don't go from the back (for why not, see "Linked List AsidLinked List Asidee"). Feel free to change to the signature of the function or use a helper function with a different signature! (hint: that means you can make your function take more arguments - ex: `lastIndexOf(5, [1,2,3], 0)`
lastIndexOf(5, [1, 2, 4, 6, 5, 2, 7]) -> 4
lastIndexOf(5, [1, 2, 4, 6, 2, 7]) -> -1
lastIndexOf(5, [1, 2, 5, 4, 6, 5, 2, 7]) -> 5
"""
def LastIndexOf(checkNum, numbers,index = 0, maxDex=-1):
	if numbers == []:#basecase to handle empty list
		return maxDex
# expand list and check each number if it's checkNum, if so keep largest index.

	next_num = numbers.pop(0) #moves through list

	if next_num == checkNum:
			maxDex = index #handles  replacement of last spot.

	index += 1 #increments index forward
	return LastIndexOf(checkNum, numbers, index, maxDex)


a=[1, 2, 4, 6, 2, 7]
b=[1, 2, 5, 4, 6, 5, 2, 7]
c=[2,4,6,3]
d = []
print LastIndexOf(5,a)
print LastIndexOf(5,b)
print LastIndexOf(5,c)
print LastIndexOf(5,d)