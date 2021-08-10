from flask import Flask, request, render_template

from Forms import SignupForm, LoginForm

from DataValidations import loginValidation
from Data_Ingestion import SignupUserIngestion
from flask.helpers import flash

from werkzeug.utils import redirect







app = Flask(__name__)
app.secret_key = 'asrtarstaursdlarsn'


@app.route('/home')
def home():

    homepage = True

    return render_template('home.html',homepage=homepage)




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

    if request.method == "POST" :


        if loginform.validate_on_submit():

            loginValidation(request.form)

            return redirect('/dashboard')

    return render_template('Login.html',loginpage= loginpage, loginform = loginform)





@app.route('/dashboard',methods=["GET", "POST"])
def dashboard():

    dashboard = "true"

    return "<h1>welcome<h1>"






if __name__ == "__main__":
    app.run( debug=True, port=5000)
