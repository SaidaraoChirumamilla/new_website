from flask import Flask, request, render_template, session
from flask_session import Session

from Python_templates import Forms,Data_Ingestion,DataValidations

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
    homepage = True

    if session['loggedin'] == True:
        return render_template('home.html',homepage=homepage)
    
    return render_template('home.html',homepage=homepage)




@app.route('/signup',methods=["GET", "POST"])
def signup():

    signuppage = "true"

    signupform = Forms.SignupForm()

    if request.method == "POST" :

        if signupform.validate_on_submit():

            message = Data_Ingestion.SignupUserIngestion(request.form)

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
    loginform = Forms.LoginForm()

    if request.method == "POST" :
        if loginform.validate_on_submit():
            message,loginuser = DataValidations.loginValidation(request.form)
            if message == 1:
                session['id'] = loginuser['id']
                session['role'] = loginuser['rol']
                session['loggedin'] = True
                flash(f'successfully logged in')
                return redirect('/')
            else:
                flash(f'please check the email and password')
                return redirect("/login")
    return render_template('Login.html',loginpage= loginpage, loginform = loginform)





@app.route('/instructor',methods=["GET", "POST"])
def instructor():
    Instructer_page = True
    

    return render_template('Instructor.html',Instructer_page=Instructer_page)



@app.route('/logout',methods=["GET", "POST"])
def logout():
    session['loggedin'] = False
    return redirect("/login")






if __name__ == "__main__":
    app.run( debug=True, port=5000)
