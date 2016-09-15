import dotproduct
import crossproduct
from inputmenu import Menu

def main():
	m1 = Menu("Vector Functions", ["Dot Product", "Cross Product"])
	m1.get_input()
	functionName = m1.get_result()
	if functionName == "Dot Product":
		success(functionName)
		dotproduct.main()
	elif functionName == "Cross Product":
		success(functionName)
		crossproduct.main()
	else:
		print("Menu returned unavailable function.")

def success(name):
	print("Entering " + name)


if __name__=="__main__":
	main()