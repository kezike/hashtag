
import database
import hashlib
import collections

sha1= hashlib.sha1()

def addPerson(username, password, fname, lname, status):
	sha1.update(password)
	if usernameAvailable(username):
		sql = """INSERT INTO person(username,
	    password, fname, lname, status)
	    VALUES ('%s', '%s', '%s', '%s', '%s');""" % (username, sha1.hexdigest(), fname, lname, status)
		cursor = database.execute(sql)
		cursor = database.execute("""SELECT id FROM person WHERE username = '%s';""" % username)
		person_id = cursor.fetchone()[0]
		return person_id
	return None

def addMatch(mentorId, menteeId):
	if mentorId!=menteeId:
		sql = """INSERT INTO matches(mentorId,
	    menteeId)
	    VALUES ('%d', '%d')""" % (mentorId, menteeId)
		database.execute(sql)
		return True
	return False

def getId(username):
	cursor = database.execute("""SELECT id FROM person WHERE username = '%s';""" % username)
	person_id = cursor.fetchone()[0]
	return person_id


def addDescription(personId, blurb, income, interest, religion, ethnicity,age, sex, education):
	sql = """INSERT INTO description(personId, blurb,
    income, interest, religion, ethnicity, age, sex, education)
    VALUES ('%d','%s', '%s','%s', '%s', '%s', '%s','%s','%s')""" % (personId, blurb, income, interest, religion, ethnicity, age, sex, education)
	database.execute(sql)
	return True

def usernameAvailable(username):
	sql = "SELECT * FROM person WHERE username='%s'" % (username)
	cursor = database.execute(sql)
	if cursor != None:
		return not cursor.fetchone()
	return False

def login(username, password):
	sha1.update(password)
	sql = """SELECT * FROM person WHERE username = '%s'""" % (username)
	cursor = database.execute(sql)
	print cursor.rowcount
	if cursor.rowcount == 1:
		data= cursor.fetchone()
		user= {}
		if sha1.hexdigest() == str(data[2]):
			user['id']=(data[0])
			user['username']=(data[1])
			user['fname']=(data[3])
			user['lname']=(data[4])
			user['status']=(data[5])
			print user
			return user
	return None

def getIds(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest):
	personIds = """SELECT personId FROM description
	WHERE age = '%s'
	AND sex = '%s'
	AND religion = '%s'
	AND ethnicity = '%s'
	AND income = '%s'
	AND education = '%s'
	AND interest = '%s'""" % (thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest)
	cursor = database.execute(personIds)
	rows = cursor.fetchall()
	data = []
	for row in rows:
		data.append(int(row[0]))
	return data

def getMentors(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest):
	data = getIds(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest)
	profiles ={}
	for pId in data:
		print pId;
		profiles[pId]= getProfile(pId)
	return profiles

def getProfile(pId):
	profile = {}
	profile['blurb']= getBlurb(pId)
	#profile['photo']= getPhoto(pId)
	profile['lname'] = getFname(pId)
	profile['fname'] = getLname(pId)
	profile['interest']= getInterest(pId)
	return profile

def getBlurb(pId):
	sql = """SELECT DISTINCT blurb from description join person WHERE personId='%d' AND status='mentor' """ % (pId)
	cursor= database.execute(sql)
	if cursor.rowcount ==1:
		return cursor.fetchone()[0]
	return None

def getPhoto(pId):
	sql = """SELECT DISTINCT photo from description join person WHERE personId='%d' AND status='mentor'""" % (pId)
	cursor= database.execute(sql)
	if cursor.rowcount ==1:
		return cursor.fetchone()[0]
	return None

def getInterest(pId):
	sql = """SELECT DISTINCT interest from description join person WHERE personId='%d' AND status='mentor' """ % (pId)
	cursor= database.execute(sql)
	if cursor.rowcount ==1:
		return cursor.fetchone()[0]
	return None

def getFname(pId):
	sql = """SELECT fname from person WHERE id='%d' AND status='mentor'""" % (pId)
	cursor= database.execute(sql)
	if cursor.rowcount ==1:
		return cursor.fetchone()[0]
	return None

def getLname(pId):
	sql= """SELECT lname from person WHERE id='%d' AND status='mentor'"""  % (pId)
	cursor= database.execute(sql)
	if cursor.rowcount ==1:
		return cursor.fetchone()[0]
	return None



