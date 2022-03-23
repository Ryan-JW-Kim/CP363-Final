
class MySqlConnection:
	def __init__(self, user, password, host="localhost"):

		# Connect to a MySQL database		
		self.db = mysql.connector.connect(host=host, user=user, password=password)

		# Initialize a cursor object that executes SQL operations
		self.cursor = self.db.cursor()

	def execute(self, commandString):
		self.cursor.execute(commandString)

		return None

	def print_tables(self):
		self.execute("SHOW TABLES")

		for table in self.cursor:
			print(table)

	