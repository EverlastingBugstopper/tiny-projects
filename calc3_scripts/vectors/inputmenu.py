class Menu:
	def __init__(self, title="Menu", options=["Option 1", "Option 2"]):
		self.options = options
		self.result = -1
		self.title = title
	def __str__(self):
		result = ""
		self.options.append(self.title)
		maxLength = int(len(max(self.options, key=len)) + len(str(len(self.options))))
		dashes = int((maxLength - (len(self.title) - 2)) / 2)
		self.options.remove(self.title)
		for dash in range(dashes):
			result += "-"
		result += " " + str(self.title) + " "
		for dash in range(dashes):
			result += "-"
		result += "\n"
		for index, option in enumerate(self.options):
			result += str(index + 1) + ": " + option + "\n"
		for dash in range((dashes * 2) + len(self.title) + 2):
			result += "-"
		result += "\n"
		return result
	def get_input(self):
		print(self.__str__())
		self.result = int(input("Enter the number of your choice: ")) - 1
	def get_result(self):
		if (self.result < 0):
			print("Invalid choice: " + str(self.result))
		else:
			return self.options[self.result]