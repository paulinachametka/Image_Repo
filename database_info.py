
import mysql.connector, os


def drop_table(): 

    #f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    #words = f.read().split()
    db_user = os.getenv("db_user", "optional-default")
    db_password = os.getenv("db_password", "optional-default")
    db_host = os.getenv("db_host", "optional-default")
    db_db = os.getenv("db_db", "optional-default")


    mydb = mysql.connector.connect(
    host=db_host,
    user= db_user,
    password=db_password,
    database=db_db
    )


    mycursor = mydb.cursor()
    sql = "DROP TABLE images"
    mycursor.execute(sql)

def create_table(): 
    #f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    #words = f.read().split()
    db_user = os.getenv("db_user", "optional-default")
    db_password = os.getenv("db_password", "optional-default")
    db_host = os.getenv("db_host", "optional-default")
    db_db = os.getenv("db_db", "optional-default")

    mydb = mysql.connector.connect(
    host=db_host,
    user= db_user,
    password=db_password,
    database=db_db
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))")



def insert_data(name,path): 

    #f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    #words = f.read().split()
    db_user = os.getenv("db_user", "optional-default")
    db_password = os.getenv("db_password", "optional-default")
    db_host = os.getenv("db_host", "optional-default")
    db_db = os.getenv("db_db", "optional-default")


    mydb = mysql.connector.connect(
    host=db_host,
    user= db_user,
    password=db_password,
    database=db_db
    )


    mycursor = mydb.cursor()
    
    sql = "INSERT INTO images (name, path) VALUES (%s, %s)"
    title = "images/" + name + '.png'
    val = (name, path)
    mycursor.execute(sql, val)
    mydb.commit()

    #print(mycursor.rowcount, "record inserted.")


def query_data():

    #f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    #words = f.read().split()
    db_user = os.getenv("db_user", "optional-default")
    db_password = os.getenv("db_password", "optional-default")
    db_host = os.getenv("db_host", "optional-default")
    db_db = os.getenv("db_db", "optional-default")


    mydb = mysql.connector.connect(
    host=db_host,
    user= db_user,
    password=db_password,
    database=db_db
    )


    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM images")
    myresult = mycursor.fetchall()



    #mycursor = mydb.cursor()


    #for x in myresult:
    #  print(x)

    #sql = "DROP TABLE images"

    #mycursor.execute(sql)

    #mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))")

def delete_image(): 

    #f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    #words = f.read().split()
    db_user = os.getenv("db_user", "optional-default")
    db_password = os.getenv("db_password", "optional-default")
    db_host = os.getenv("db_host", "optional-default")
    db_db = os.getenv("db_db", "optional-default")


    mydb = mysql.connector.connect(
    host=db_host,
    user= db_user,
    password=db_password,
    database=db_db
    )


    mycursor = mydb.cursor()

    sql = "DELETE FROM images WHERE name = 'lend'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


create_table()