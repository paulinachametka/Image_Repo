from flask import Flask, render_template
import mysql.connector, os
from getpass import getpass
from image_generator import *

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


generate_image()

mycursor = mydb.cursor()
mycursor.execute("SELECT path FROM images")

image_paths = mycursor.fetchall()

mycursor.execute("SELECT * FROM images")

all_info = mycursor.fetchall()
#print(all_info)



app = Flask(__name__)

@app.route("/")
def hello_world():
    #return render_template('index.html', image=image) 
    info = image_paths
    return render_template('index.html',info = info,all_info= all_info )




#mycursor = mydb.cursor()

#sql = "INSERT INTO images (name, path) VALUES (%s, %s)"
#val = ("Art 1", r"C:\Users\pauli\Documents\GitHub\Image_Repo\images\image.png")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

