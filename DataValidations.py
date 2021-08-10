import psycopg2

connection = psycopg2.connect(user="teja",
                                  password="Saidarao3!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iamstem")


   # Create a cursor to perform database operations
cursor = connection.cursor()

def loginValidation(form):

    cursor.execute("SELECT FROM users where email = %s",(form['email'],))

    loginuser = cursor.fetchall()

    print(loginuser)
