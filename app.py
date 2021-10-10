from flask import Flask, request, render_template, session
from flask_session import Session

from Forms import SignupForm, LoginForm

from DataValidations import loginValidation
from Data_Ingestion import SignupUserIngestion
from flask.helpers import flash

from werkzeug.utils import redirect



app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
app.secret_key = 'asrtarstaursdlarsn'



@app.route('/')
def home():

    print(session)

    if session['loggedin'] == True:
        return render_template('dashboard.html',loggedin = currentuser['loggedin'],role = role)
    homepage = True
    return render_template('dashboard.html',homepage=homepage)




@app.route('/signup',methods=["GET", "POST"])
def signup():

    signuppage = "true"

    signupform = SignupForm()

    if request.method == "POST" :

        if signupform.validate_on_submit():

            message = SignupUserIngestion(request.form)

            if message == 1:

                flash(f'Account Created succesfully for  {signupform.firstname.data} please login here ')

                return redirect('/home')
            else :
                flash(f'Email Already Exists create with new email or login with the {signupform.email.data}')

                return redirect("/signup")

    return render_template('signup.html',signuppage=signuppage, signupform = signupform)





@app.route('/login',methods=["GET", "POST"])
def login():

    loginpage = "true"

    loginform = LoginForm()

    print(loginform)

    if request.method == "POST" :

        if loginform.validate_on_submit():

            message,loginuser = loginValidation(request.form)

            if message == 1:

                session['id'] = loginuser['id']
                session['role'] = loginuser['rol']
                session['loggedin'] = True
                print(session)

                flash(f'successfully logged in')

                return redirect('/dashboard')

            else:
                flash(f'please check the email and password')

                return redirect("/login")

    print(loginform)


    return render_template('Login.html',loginpage= loginpage, loginform = loginform)




@app.route('/dashboard',methods=["GET", "POST"])
def dashboard():

    dashboard = "true"
    print(currentuser)
    if currentuser['rol'] == 'Student':
        global role
        role = 'Student'
    else :
        role = "instructor"

    return render_template('dashboard.html',loggedin = currentuser['loggedin'],role = role)


@app.route('/instructor',methods=["GET", "POST"])
def instructor():
    Instructer_page = True
    print(currentuser)
    if currentuser['rol'] == 'Student':
        global role
        role = 'Student'
    else :
        role = "instructor"

    return render_template('Instructor.html',loggedin = currentuser['loggedin'],role = role)



@app.route('/logout',methods=["GET", "POST"])
def logout():
    if currentuser is not None :
        currentuser['loggedin'] = False
    return redirect("/login")






if __name__ == "__main__":
    app.run( debug=True, port=5000)
