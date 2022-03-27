
class UserInput:

	def __init__(self):
		self.breakpoint = False

	def receive_command(self) -> dict:
		"""
		UserInput.receive_command() called in main.py this method uses python's input() method
		to generate a dictionary containing user query data.
		"""

		myDict = {}

		msg = "Add, Remove, CreateTable, Select, CreateDatabase -> "
		command = input(msg)
		print()

		if command == "Remove":

			myDict["type"] = "Remove"

			msg = "Librarian, Book, User, Section -> "
			command = input(msg)

			if command == "Librarian" or command == "Book" or command == "User" or command == "Section":

				msg = f"ID of {command} to DELETE ->"
				id = input(msg)

				myDict["target"] = command
				myDict["id"] = id

			else:
				print("Error")
				self.breakpoint = True

		elif command == "Add":

			myDict["type"] = "Add"
			myDict["target"] = None
			msg = "Librarian, Book, User, Section -> "
			command = input(msg)

			if command == "Librarian":

				fname = input("Librarian\'s first name ->")
				lname = input("Librarian\'s last name -> ")
				sectionID = input(f"Section ID managed by librarian ->")
				librarianID = input("Librarian ID ->")

				myDict["target"] = command
				myDict["first_name"] = fname
				myDict["last_name"] = lname
				myDict["section_ID"] = sectionID
				myDict["librarian_ID"] = librarianID

			elif command == "Book":
				
				genre = input("Genre -> ")
				title = input("Title -> ")
				publisher = input("Publisher -> ")
				author = input("Author -> ")
				yearPublished = input("Year Published -> ")
				sectionID = input("What sectionID does this belong too -> ")
				eNumber = input("Edition Number -> ")
				bookID = input("What is the bookID -> ")				

				myDict["bookID"] = bookID
				myDict["target"] = command
				myDict["genre"] = genre
				myDict["title"] = title
				myDict["publisher"] = publisher
				myDict["author"] = author
				myDict["year_published"] = yearPublished 
				myDict["section_ID"] = sectionID
				myDict["edition_number"] = eNumber				

			elif command == "User":
				
				userID = input("User ID -> ")
				fname = input("User\'s first name -> ")
				lname = input("User\'s last name -> ")
				email = input("User\'s email address -> ")
				telephone = input("User\'s telephone number -> ")
				address = input("User\'s address -> ")
				pCode = input("User\'s postal code -> ")
				city = input("User\'s city -> ")
				userSince = datetime.now().date().__str__()
				overDue = 0

				myDict["target"] = command
				myDict["first_name"] = fname
				myDict["last_name"] = lname
				myDict["email"] = email
				myDict["telephone"] = telephone
				myDict["address"] = address
				myDict["postal_code"] = pCode
				myDict["city"] = city
				myDict["user_ID"] = userID
				myDict["user_since"] = userSince
				myDict["overdue"] = overDue

			elif command == "Section":
				
				sectionID = input("Section ID -> ")
				librarianID = input("Librarian ID -> ")

				myDict["target"] = command
				myDict["section_ID"] = sectionID 
				myDict["librarian_ID"] = librarianID 

			else:
				print("Error")
				self.breakpoint = True

		elif command == "CreateTable":

			myDict["type"] = "CreateTable"

			msg = "Librarian, Book, User, Section -> "
			command = input(msg)

			if command == "Librarian" or command == "Book" or command == "User" or command == "Section":
				myDict["target"] = command

			else:
				print("Error")
				self.breakpoint = True

		elif command == "Select":

			myDict["type"] = "Select"

			msg = "Librarian, Book, User, Section -> "
			command = input(msg)

			if command == "Librarian" or command == "Book" or command == "User" or command == "Section":

				myDict["target"] = command

				msg = f"ID of {command} to SELECT ->"
				command = input(msg)

				myDict["id"] = command

		elif command == "CreateDatabase":
			myDict["type"] = "CreateDatabase"

		else:
			print("Error, expected one of five choices (Add Remove CreateTable Select CreateDatabase)")
			self.breakpoint = True

		return myDict

	def parse_to_SQL(self, command: dict) -> str:
		"""
		UserInput().parse_to_SQL(cmd) called in main.py this method uses a dictionary created
		through UserInput.receive_command() to generate a string representing a SQL query to be
		passed to the mysql.connector.connect().cursor().execute(QUERY) method.
		"""

		rtn_str = None

		if "type" not in command.keys():
			print("Error, unexpepected key")
			self.breakpoint = True

		elif command["type"] == "Add":

			if command["target"] == "Book":

				_id = command["bookID"]
				title = command["title"]
				author = command["author"]
				publisher = command["publisher"]
				year_published = command["year_published"]
				eNum = command["edition_number"]
				genre = command["genre"]
				sectionID = command["section_ID"]

				rtn_str = f"INSERT INTO library.book(\'{_id}\', \'{title}\', \'{author}\', \'{publisher}\', \'{year_published}\', \'{eNum}\', \'{genre}\', \'available\', \'{sectionID}\')"

			elif command["target"] == "User":

				_id = command["user_ID"]
				fname = command["first_name"]
				lname = command["last_name"] 
				email = command["email"]
				telephone = command["telephone"]
				address = command["address"]
				pCode = command["postal_code"]
				city = command["city"]
				userSince = command["user_since"]
				overDue = command["overdue"]

				rtn_str = f"INSERT INTO library.user(\'{_id}\', \'{email}\', \'{telephone}\', \'{address}\', \'{pCode}\', \'{city}\', \'{userSince}\', \'{overDue}\')"

			elif command["target"] == "Section":

				_id = command["section_ID"]
				librarianID = command["librarian_ID"]

				rtn_str = f"INSERT INTO library.section(\'{_id}\', \'{librarianID}\')"

			elif command["target"] == "Libarian":

				fname = command["first_name"]
				lname = command["last_name"]
				sectionID = command["section_ID"]
				librarianID = command["librarian_ID"]

				rtn_str = f"INSERT INTO library.librarian(\'{fname}\', \'{lname}, \'{sectionID}\', \'{librarianID}\')"
			
			else:
				print("Error")
				self.breakpoint = True

		elif command["type"] == "Remove":

			if command["target"] == "Book":

				_id = command["id"]
				rtn_str = f"DELETE FROM library.book WHERE BOOK_ID=\'{_id}\'"

			elif command["target"] == "User":

				_id = command["id"]
				rtn_str = f"DELETE FROM library.user WHERE USER_ID=\'{_id}\'"

			elif command["target"] == "Section":

				_id = command["id"]
				rtn_str = f"DELETE FROM library.section WHERE SECTION_ID=\'{_id}\'"

			elif command["target"] == "Libarian":

				_id = command["id"]
				rtn_str = f"DELETE FROM library.librarian WHERE SECTION_ID=\'{_id}\'"

			else:
				print("Error")
				self.breakpoint = True

		elif command["type"] == "Select":

			if "target" not in command.keys():
				print("Error, unexpected key")
				self.breakpoint = True

			elif command["target"] == "Book":

				_id = command["id"]
				rtn_str = f"SELECT * FROM library.book WHERE BOOK_ID=\'{_id}\'"

			elif command["target"] == "User":

				_id = command["id"]
				rtn_str = f"SELECT * FROM library.user WHERE USER_ID=\'{_id}\'"

			elif command["target"] == "Section":

				_id = command["id"]
				rtn_str = f"SELECT * FROM library.section WHERE SECTION_ID=\'{_id}\'"

			elif command["target"] == "Libarian":

				_id = command["id"]
				rtn_str = f"SELECT * FROM library.librarian WHERE LIBRARIAN_ID=\'{_id}\'"

			else:
				print("Error")
				self.breakpoint = True

		elif command["type"] == "CreateTable":

			if command["target"] == "Book":
				rtn_str = "CREATE TABLE `book` (`BOOK_ID` int NOT NULL, `TITLE` varchar(100) NOT NULL, `AUTHOR` varchar(100) NOT NULL, `PUBLISHER` varchar(100) NOT NULL, `YEAR_PUBLISHED` int NOT NULL, `EDITION_NUM` varchar(100) NOT NULL, `GENRE` varchar(100) NOT NULL, `STATUS` varchar(30) NOT NULL, `SECTION_ID` int NOT NULL, PRIMARY KEY (`BOOK_ID`))"

			elif command["target"] == "User":
				rtn_str  = "CREATE TABLE `user` (`USER_ID` int NOT NULL, `FIRST_NAME` varchar(100) NOT NULL, `LAST_NAME` varchar(100) NOT NULL, `EMAIL` varchar(100) NOT NULL, `TELEPHONE` bigint NOT NULL, `ADDRESS` varchar(100) NOT NULL, 'POSTAL_CODE` varchar(6) NOT NULL, `CITY` varchar(100) NOT NULL,`USER_SINCE` date NOT NULL, `OVERDUE_AMOUNT` decimal(19,2) NOT NULL, PRIMARY KEY (`USER_ID`))"

			elif command["target"] == "Section":
				rtn_str = "CREATE TABLE `section` (`SECTION_ID` int NOT NULL, `LIBRARIAN_ID` int NOT NULL, PRIMARY KEY (`SECTION_ID`)"

			elif command["target"] == "Librarian":
				rtn_str = "CREATE TABLE `librarian` (`LIBRARIAN_ID` int NOT NULL, `FIRST_NAME` varchar(100) NOT NULL, `LAST_NAME` varchar(100) NOT NULL, `RESPONSIBILITY` varchar(100) NOT NULL, `START_TIME` time NOT NULL, `END_TIME` time NOT NULL, PRIMARY KEY (`LIBRARIAN_ID`))"
			
			else:
				print("Error")
				self.breakpoint = True

		elif command["type"] == "CreateDatabase":
			rtn_str = "CREATE DATABASE LIBRARY"

		else:
			print("Error, expected one of five choices (Add Remove CreateTable Select CreateDatabase)")
			self.breakpoint = True

		return rtn_str


