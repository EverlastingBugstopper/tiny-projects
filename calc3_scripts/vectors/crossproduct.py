from vector import Vector

def main():
	cross_product(get_input())

def get_input():
	v1 = Vector()
	v2 = Vector()
	v1.get_input("1")
	v2.get_input("2")
	return (v1, v2)

def cross_product(vectors):
	vector1 = vectors[0]
	vector2 = vectors[1]
	xList = [str(vector1.x), str(vector2.x)]
	yList = [str(vector1.y), str(vector2.y)]
	zList = [str(vector1.z), str(vector2.z)]
	xLength = len(max(xList, key=len))
	yLength = len(max(yList, key=len))
	zLength = len(max(zList, key=len))
	xLength = (xLength + (xLength % 2)) + 1
	yLength = (yLength + (yLength % 2)) + 1
	zLength = (zLength + (zLength % 2)) + 1
	width = 2 + zLength + yLength + xLength
	row_break(width)
	column_break()
	center_padding("i", xLength)
	column_break()
	center_padding("j", yLength)
	column_break()
	center_padding("k", zLength)
	column_break()
	print()
	for vector in vectors:
		column_break()
		right_padding(vector.x, xLength)
		column_break()
		right_padding(vector.y, yLength)
		column_break()
		right_padding(vector.z, zLength)
		column_break()
		print()
	row_break(width)

def right_padding(string, padding):
	print('{{0: >{}}}'.format(int(padding)).format(str(string)), end="")

def center_padding(string, padding):
	print('{{0: ^{}}}'.format(int(padding)).format(str(string)), end="")

def column_break():
	right_padding("|", 1)

def row_break(dashes):
	print (' ', end = "")
	for i in range(dashes):
		print('-', end="")
	print (' ', end = "")
	print()

if __name__ == '__main__':
	main()