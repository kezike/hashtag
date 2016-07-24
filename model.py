import database
import hashlib

sha1= hashlib.sha1()

def addPerson(username, password, fname, lname):
	sha1.update(password)
	sql = """INSERT INTO person(username,
    password, fname, lname)
    VALUES ('%s', '%s', '%s', '%s')""" % (username, sha1.hexdigest(), fname, lname)
	database.execute(sql)

def addMatch(mentorId, menteeId):
	sql = """INSERT INTO matches(mentorId,
    menteeId)
    VALUES ('%d', '%d')""" % (mentorId, menteeId)
	database.execute(sql)

def addDescription(personId, blurb, income, interest, religion, ethnicity,age, sex, education):
	sql = """INSERT INTO description(personId, blurb,
    income, intrest, religion, ethnicity, age, sex, education)
    VALUES ('%d','%s', '%s','%s', '%s', '%s', '%s','%s','%s')""" % (personId, blurb, income, interest, religion, ethnicity, age, sex, education)
	database.execute(sql)

def getProfiles(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest) {
	personIds = """SELECT personId FROM description
	WHERE age=thisAge
	AND sex=thisSex
	AND religion=thisReligion
	AND ethnicity=thisEthnicity
	AND income=thisIncome
	AND education=thisEducation
	AND interest=thisInterest"""
	database.execute(personIds)

	placeholder = ','
	personIdStrings = ','.join(placeholder * len(personIds))
	sql = "SELECT * FROM person WHERE id IN (%s)" % personIdStrings
	database.execute(sql)
}
