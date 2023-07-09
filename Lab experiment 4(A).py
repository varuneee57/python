'''TUPLES AND
ITS
OPERATION'''
a. Write a python program to convert tuple to a string

def convertTuple(tup):
		# initialize an empty string
	str = ''
	for item in tup:
		str = str + item
	return str


# Driver code
tuple = ('p', 'y', 't', 'h', 'o', 'n')
str = convertTuple(tuple)
print(str)
