import database
# Create table as per requirement
person = """CREATE TABLE person (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username CHAR(20) NOT NULL,
	password CHAR(50) NOT NULL,
	fname CHAR(20),
	lname CHAR(20))"""

description = """CREATE TABLE description (
	personId INT NOT NULL,
	blurb CHAR(150) NOT NULL,
	income CHAR(20),
	interest CHAR(50),
	religion CHAR(20),
	ethnicity CHAR(20),
    age CHAR(10),  
    sex CHAR(10),
	education CHAR(20))"""

matches = """CREATE TABLE matches (
	mentorId  INT NOT NULL,
	menteeId  INT NOT NULL)"""

database.execute(person)
database.execute(description)
database.execute(matches)
