
class UserInput:

	def __init__(self):
		self.comamnds = []

	def reportSucess(self, command: dict):
		pass

	def reportFailure(self, command: dict):
		pass

	def get_command(self) -> dict:
		pass

	def get_parameters(self, command: dict) -> dict:
		
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
