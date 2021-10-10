import psycopg2
# import sys
from psycopg2.extras import RealDictCursor

connection = psycopg2.connect(user="teja",
                                  password="Saidarao3!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iamstem",
                                  cursor_factory=RealDictCursor)


   # Create a cursor to perform database operations
cursor = connection.cursor()

def loginValidation(form):

    cursor.execute("SELECT * FROM users where email = %s",(form['email'],))

    loginuser = cursor.fetchall()


    if len(loginuser) ==0:
        return 0,loginuser[0]
    elif form['email'] == loginuser[0]['email'] and form['password'] == loginuser[0]['pass']:

        return 1,loginuser[0]

    else :
        return 0,loginuser[0]
        

