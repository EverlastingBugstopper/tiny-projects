class Vector:
	def __init__(self, x=0, y=0, z=0):
		self.x=x
		self.y=y
		self.z=z

	def get_input(self, num=""):
		self.x = float(input("x" + num + ": "))
		self.y = float(input("y" + num + ": "))
		self.z = float(input("z" + num + ": "))

	def __str__(self):
		return "<" + str(self.x) + ", " + str(self.y) + ", " + str(self.z) + ">"

if __name__ == "__main__":
	print("This is the class for vectors. No scripts are run here.")
