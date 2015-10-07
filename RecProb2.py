#Find largest number in a list

def max(numbers, largest_so_far=0):
	if numbers == []: #handles if there's an empty array, returns 0	
		return largest_so_far
	next_num = numbers.pop(0) #designates next_num as first element 
	    #and pops first element out of numbers zero pops beginning, empty brackets pops end.
	if next_num > largest_so_far: #checks if next_numis larger 
	    #and if so passes numbers and next_num on to a recursive call.
		return max(numbers, next_num)
	else: #if next_num is smaller passes numbers  and largest_so_far
		return max(numbers, largest_so_far)

a=[1,4,6,2,9,3]
print max (a)

"""
accumulator=the variable that 
tracks the results through the recursive function.
reduce = take list and do an operation into one value. 
summing is a reduce, max is a reduce, min is a reduce.
"""