
import mysql.connector, os


def drop_table(): 

    f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    words = f.read().split()
    db_user = words[0]
    db_password = words[1]

    mydb = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_password,
    database="dbimages"
)

    mycursor = mydb.cursor()
    sql = "DROP TABLE images"
    mycursor.execute(sql)

def create_table(): 
    f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    words = f.read().split()
    db_user = words[0]
    db_password = words[1]

    mydb = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_password,
    database="dbimages"
)

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))")



def insert_data(name,path): 

    f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    words = f.read().split()
    db_user = words[0]
    db_password = words[1]


    mydb = mysql.connector.connect(
    host="localhost",
    user= db_user,
    password=db_password,
    database="dbimages"
    )

    mycursor = mydb.cursor()
    
    sql = "INSERT INTO images (name, path) VALUES (%s, %s)"
    title = "images/" + name + '.png'
    val = (name, path)
    mycursor.execute(sql, val)
    mydb.commit()

    #print(mycursor.rowcount, "record inserted.")





def query_data():

    f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    words = f.read().split()
    db_user = words[0]
    db_password = words[1]


    mydb = mysql.connector.connect(
    host="localhost",
    user= db_user,
    password=db_password,
    database="dbimages"
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

    f = open('C:/Users/pauli/Desktop/credentials.txt', "r")
    words = f.read().split()
    db_user = words[0]
    db_password = words[1]

    mydb = mysql.connector.connect(
    host="localhost",
    user=db_user,
    password=db_password,
    database="dbimages"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM images WHERE name = 'fresh'"

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")

delete_image()