
import database
import hashlib
import collections

sha1= hashlib.sha1()

def addPerson(username, password, fname, lname):
	sha1.update(password)
	if usernameAvailable(username):
		sql = """INSERT INTO person(username,
	    password, fname, lname)
	    VALUES ('%s', '%s', '%s', '%s')""" % (username, sha1.hexdigest(), fname, lname)
		database.execute(sql)
		return True
	return False

def addMatch(mentorId, menteeId):
	if mentorId!=menteeId:
		sql = """INSERT INTO matches(mentorId,
	    menteeId)
	    VALUES ('%d', '%d')""" % (mentorId, menteeId)
		database.execute(sql)
		return True
	return False
	

def addDescription(personId, blurb, income, interest, religion, ethnicity,age, sex, education):
	sql = """INSERT INTO description(personId, blurb,
    income, intrest, religion, ethnicity, age, sex, education)
    VALUES ('%d','%s', '%s','%s', '%s', '%s', '%s','%s','%s')""" % (personId, blurb, income, interest, religion, ethnicity, age, sex, education)
	database.execute(sql)

def usernameAvailable(username):
	sql = """SELECT * FROM person WHERE username='%s'""" % (username)
	cursor = database.execute(sql)
	if cursor.fetchone()[0] == 0:
		return True
	return False

def login(username, password):
	sha1.update(password)
	sql = """SELECT * FROM person WHERE username = '%s'""" % (username)
	cursor = database.execute(sql)
	if cursor.rowcount == 1:
		data= cursor.fetchone()
		user= {}
		if sha1.hexdigest() == str(data[2]):
			user['id']=data[0]
			user['username']=(data[1])
			user['fname']=(data[3])
			user['name']=(data[4])
			return user
	return None

def getProfiles(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest):
	personIds = """SELECT personId FROM description
	WHERE age = thisAge
	AND sex = thisSex
	AND religion = thisReligion
	AND ethnicity = thisEthnicity
	AND income = thisIncome
	AND education = thisEducation
	AND interest = thisInterest"""
	cursor = database.execute(personIds)
	rows = cursor.fetchall()
	data = []
	for row in rows:
		data.append(cursor["personId"])
	return data