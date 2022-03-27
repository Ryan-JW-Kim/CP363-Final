
class FakeConnect:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password

	def cursor(self):
		return Cursor()

class Cursor:
	def __init__(self):
		pass

	def execute(self, operation, params=None, mulit=False):
		return None		

class MySqlConnection:
	def __init__(self, user, password, host="localhost"):

		# Connect to a MySQL database		
		self.db = FakeConnect(host, user, password) # self.db = mysql.connector.connect(host=host, user=user, password=password)

		# Initialize a cursor object that executes SQL operations
		self.cursor = self.db.cursor()

	def execute(self, commandString):

		# Perform neccesary checks
		if commandString == None or commandString == "":
			return False

		else:
			self.cursor.execute(commandString)
			return True


