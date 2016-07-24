import MySQLdb

con= {'host': 'hashtag.ccyevrvcqxia.us-west-2.rds.amazonaws.com',
  'username': 'hashtag',
  'password': 'hashtag2040',
  'db': 'hashtag'}

db = MySQLdb.connect(con['host'],con['username'],con['password'], con['db'])
db.autocommit(True)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

def execute(sql):
	cursor.execute(sql)
	return cursor	
