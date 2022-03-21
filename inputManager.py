
class UserInput:

	def __init__(self):
		self.comamnds = []

	def get_command() -> dict:
		pass

	def get_parameters(command: dict) -> dict:
		
		if command["type"] == "view":
			pass

			if command["target"] == "book":
				pass

			elif command["target"] == "librarian":
				pass

			elif command["target"] == "user":
				pass

			elif command["target"] == "section":
				pass

			else:
				pass

		elif command["type"] == "add":
			pass

			if command["target"] == "book":
				pass

			elif command["target"] == "librarian":
				pass

			elif command["target"] == "user":
				pass

			elif command["target"] == "section":
				pass

			else:
				pass


		elif command["type"] == "remove":
			pass

			if command["target"] == "book":
				pass

			elif command["target"] == "librarian":
				pass

			elif command["target"] == "user":
				pass

			elif command["target"] == "section":
				pass

			else:
				pass

		elif command["type"] == "make":
			pass

			if command["target"] == "new": 
				pass

			elif command["target"] == "template":
				pass

			else:
				pass
		else:
			pass

"""
view:
	librarian
		manages where
		schedule
		general information
	book
		in section
		general information
		in stock
	user
		taken books
		general information
	section
		number of books in section
		general description

add:
	librarian

	book
	user
	section
"""