import dotproduct
import crossproduct
from inputmenu import Menu

def main():
	m1 = Menu("Vector Functions", ["Dot Product", "Cross Product"])
	m1.get_input()
	m1.get_result()


if __name__=="__main__":
	main()