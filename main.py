from userInputManager import *
from mySQLconnector import * 

USER = "USERNAME"
PASSWORD = "PASSWORD"

def main():
	
	ui = UserInput()
	SQL_connection = MySqlConnection(user=USER, password=PASSWORD)

	while ui.breakpoint == False:

		myDict = ui.receive_command()

		if ui.breakpoint == False:
			myQuery = ui.parse_to_SQL(myDict)

			print(f"\nSQL Query --> {myQuery} <--")

			code = SQL_connection.execute(myQuery)

			if code == False:
				print("		Error In Execution")

			else:
				print("		Success\n")

if __name__ == "__main__":

	print(f"----Starting User-DB interaction----\n")
	main()
	print(f"\n----Ending User-DB interaction------")


