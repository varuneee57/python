'''TUPLES AND
ITS
OPERATION'''

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
