# import the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash, abort
import model

# create the application object
app = Flask(__name__ ,static_url_path='')

# use decorators to link the function to a url
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        user= session.get('user')
        return redirect(url_for('main'))

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        search= str(request.form['search'])
        return redirect(url_for('search'))
    return render_template('main.html')

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

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        income= str(request.form['income'])
        print income
        interest= str(request.form['interest'])
        religion= str(request.form['religion'])
        ethnicity= str(request.form['ethnicity'])
        print ethnicity
        age= str(request.form['age'])
        sex= str(request.form['sex'])
        education= str(request.form['education'])
        print education
        mentors = model.getMentors(age, sex, religion, ethnicity, income,education, interest)
        print mentors
        return render_template('match.html', mentors= mentors)
    return render_template('search.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    print "chatting"
    if request.method == 'POST' or request.method == 'GET':
        print "posted"
        return render_template('chat.html')
    return render_template('chat.html')

 # route for handling the signup page logic
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        fname= str(request.form['fname'])
        lname= str(request.form['lname'])
        status= str(request.form['status'])
        username= str(request.form['username'])
        password= str(request.form['password'])
        blurb= str(request.form['blurb'])
        income= str(request.form['income'])
        interest= str(request.form['interest'])
        religion= str(request.form['religion'])
        ethnicity= str(request.form['ethnicity'])
        age= str(request.form['age'])
        sex= str(request.form['sex'])
        education= str(request.form['education'])
        personId=model.addPerson(username, password, fname, lname, status)
        if(personId!=None):
            description = model.addDescription(personId, blurb, income, interest, religion, ethnicity,age, sex, education)
            if(description):
                session['logged_in'] = True
                return redirect(url_for('home'))
        else:
            error= 'Login already exists try another one'
            return render_template('signup.html', error = error) 
    error= 'User could not be created'
    return render_template('signup.html', error = error)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.secret_key = 'Thisisthebestappever'
    app.run(debug=True)