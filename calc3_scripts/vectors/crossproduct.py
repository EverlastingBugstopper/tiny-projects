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

	print("((%(j1)d * %(k2)d) - (%(j2)d * %(k1)d)) - ((%(i1)d * %(k2)d) - (%(i2)d * %(k1)d)) + ((%(i1)d * %(j2)d) - (%(i2)d * %(j1)d)) = " % \
		{"i1": vector1.x, "i2": vector2.x, \
		 "j1": vector1.y, "j2": vector2.y, \
		 "k1": vector1.z, "k2": vector2.z})

	i1 = vector1.y * vector2.z
	i2 = vector2.y * vector1.z
	j1 = vector1.x * vector2.z
	j2 = vector2.x * vector1.z
	k1 = vector1.x * vector2.y
	k2 = vector2.x * vector1.y

	print("(%(i1)d - %(i2)d) - (%(j1)d - %(j2)d) + (%(k1)d - %(k2)d) = " % \
		{"i1": i1, "i2": i2, \
		 "j1": j1, "j2": j2, \
		 "k1": k1, "k2": k2})

	i0 = i1 - i2
	j0 = j1 - j2
	k0 = k1 - k2

	print("%(i0)d - %(j0)d + %(k0)d = " % \
		  {"i0": i0, "j0": j0, "k0": k0})

	print(i0 - j0 + k0)

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