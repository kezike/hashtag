# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
import model

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        user= session.get('user')
        return "Hello"


  # route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username= str(request.form['username'])
        password= str(request.form['password'])
        user = model.login(username, password)
        if user == None:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['user'] = user
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

 # route for handling the signup page logic
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        fname= str(request.form['fname'])
        print fname
        lname= str(request.form['lname'])
        username= str(request.form['username'])
        password= str(request.form['password'])
        blurb= str(request.form['blurb'])
        income= str(request.form['income'])
        intrest= str(request.form['intrest'])
        religion= str(request.form['religion'])
        age= str(request.form['age'])
        sex= str(request.form['sex'])
        education= str(request.form['education'])
        print education
        person=model.addPerson(username, password, fname, lname)
        description = model.addDescription(personId, blurb, income, interest, religion, ethnicity,age, sex, education)
        if(person and description):
            session['logged_in'] = True
            return redirect(url_for('home'))
        error= 'User could not be created'
    return render_template('signup.html', error = error)

# route for handling the searchProfiles page logic
@app.route('/searchProfiles', methods=GET['GET', 'POST'])
def searchProfiles(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest):
    return render_template('match.html', interests=model.getProfiles(thisAge, thisSex, thisReligion, thisEthnicity, thisIncome, thisEducation, thisInterest))

# start the server with the 'run()' method
if __name__ == '__main__':
    app.secret_key = 'Thisisthebestappever'
    app.run(debug=True)