from flask import Flask, render_template
import mysql.connector
from getpass import getpass



app = Flask(__name__)

@app.route("/")
def hello_world():
    image = r"images/image.png" 
    return render_template('index.html', random_image=image)

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

#mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE images (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), path VARCHAR(255))")


#mycursor = mydb.cursor()

#sql = "INSERT INTO images (name, path) VALUES (%s, %s)"
#val = ("Art 1", r"C:\Users\pauli\Documents\GitHub\Image_Repo\images\image.png")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM images")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
