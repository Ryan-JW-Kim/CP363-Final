from dbManager import Database
from inputManager import UserInput

def main():

	db = Database()
	userInterface = UserInput()

	while db.is_running:

		myCommand = userInterface.get_command()

		myParameters = userInterface.get_parameters(myCommand)

		# Issues  a command and parameters to DBM class
		completed = db.issue(myCommand, myParameters)

		# if command completed
		if completed:
			pass
			userInterface.reportSucess(myCommand)

		# if command failed to complete
		else:
			pass
			userInterface.reportFailure(myCommand)


if __name__ == "__main__":

	print("Starting Program....\n")
	main()
	print("Ending Program.....\n")