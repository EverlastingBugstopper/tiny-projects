from vector import Vector

def main():
	dot_product(get_input())

def get_input():
	v1 = Vector()
	v2 = Vector()
	v1.get_input("1")
	v2.get_input("2")
	return (v1, v2)

def dot_product(vectors):
	vector1 = vectors[0]
	vector2 = vectors[1]
	print("(x1 - x2) + (y1 - y2) + (z1 - z2) = ")
	print("(%(x1)d - %(x2)d) + (%(y1)d - %(y2)d) + (%(z1)d - %(z2)d) = " % \
		{"x1": vector1.x, "x2": vector2.x, "y1": vector1.y, "y2": vector2.y, "z1": vector1.z, "z2": vector2.z})
	x = vector1.x - vector2.x
	y = vector1.y - vector2.y
	z = vector1.z - vector2.z
	print("(%(x0)d) + (%(y0)d) + (%(z0)d) = " % \
		{"x0": x, "y0": y, "z0": z})
	product = x + y + z
	print(str(product))
	if (product == 0):
		print_vectors(vector1, vector2)
		print("are perpendicular because the dot product is 0." % \
			{"vector1": vector1.__str__(), "vector2": vector2.__str__()})
	else:
		xCoeff = vector1.x / vector2.x
		yCoeff = vector1.y / vector2.y
		zCoeff = vector1.z / vector2.z
		if (xCoeff == yCoeff and xCoeff == zCoeff):
			print_vectors(vector1, vector2)
			print("are parallel because they have a scalar multiple of %(scalar)d." % \
			{"vector1": vector1.__str__(), "vector2": vector2.__str__(), "scalar": xCoeff})
		else:
			print_vectors(vector1, vector2)
			print("are skew because the dot product is not 0,\nand they are no scalar multiples of each other." % \
			{"vector1": vector1.__str__(), "vector2": vector2.__str__()})

def print_vectors(vector1, vector2):
	print("The two vectors %(vector1)s and %(vector2)s" % \
			{"vector1": vector1.__str__(), "vector2": vector2.__str__()})
if __name__=="__main__":
	main()