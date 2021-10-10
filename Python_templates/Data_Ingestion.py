import psycopg2



def SignupUserIngestion(form):
    connection = psycopg2.connect(user="teja",
                                  password="Saidarao3!",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="iamstem")


   # Create a cursor to perform database operations
    cursor = connection.cursor()


    firstname = form['firstname']
    secondname = form['secondname']
    email = form['email']
    password = form['password']
    phone = form['phone']
    role = form['role']
    grade = 't'.join(form.getlist('grade'))
    cursor.execute("SELECT email FROM users where email = %s",(email,))
    emails = cursor.fetchall()

    if len(emails) == 0:
        user_insert_query = """INSERT INTO users (firstname, lastname, email,pass,rol,phone,grade) \
            VALUES (%s,%s,%s,%s,%s,%s,%s)"""
        cursor.execute(user_insert_query,(firstname,secondname,email,password,role,phone,grade))
        connection.commit()
        return  1
    else:
        return 0


    
   