""" 
Using no loops (for, while, etc.), and no global variables, 
write a function that returns the sum of a list: 
Also, no cheating and calling methods that do significant work for you 
(i.e. sum(), reduce(), etc. are all off limits).

sum([1, 2, 3, 4, 5]) -> 15
sum([]) -> 0

"""

def SumList(numbers, Total=0):
	if numbers == []:#handles empty array with a zero retrun
		return Total
	next_num = numbers.pop()
	return next_num + SumList(numbers, Total)
b=[0]
a=[1,2,3,4,5]

print SumList(b)
print SumList(a)