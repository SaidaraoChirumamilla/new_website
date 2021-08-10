from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo



class MultiCheckboxField(SelectMultipleField):
        widget = widgets.ListWidget(prefix_label=False)
        option_widget = widgets.CheckboxInput()


class SignupForm(FlaskForm):

    role_drop_down = ["None","Student","Instructor","Admin"]

    gradeMenu = ['11','22', '33', '44']

    firstname = StringField('First name',
                           validators=[DataRequired(), Length(min=2, max=20)])

    secondname = StringField('Second name',
                           validators=[DataRequired(), Length(min=3, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired() ,Length(min=8)])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    
    phone = StringField('Phone',
                           validators=[DataRequired()])

    role = SelectField('Role', choices=role_drop_down, default=1)

    grade = MultiCheckboxField('Select Grade', choices = gradeMenu , default = 1)

    submit = SubmitField('Sign Up')

    def __init__(self, *args, **kwargs):
            kwargs['csrf_enabled'] = False
            super(SignupForm, self).__init__(*args, **kwargs)


class LoginForm(FlaskForm):

    email = StringField('Email',
                        validators=[DataRequired()])

    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Login')

    def __init__(self, *args, **kwargs):
            kwargs['csrf_enabled'] = False
            super(LoginForm, self).__init__(*args, **kwargs)

    




