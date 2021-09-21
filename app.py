from flask import Flask, render_template
import mysql.connector, os
from getpass import getpass
from image_generator import *
from database_info import *

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


#generate_image()

#mycursor = mydb.cursor()
#mycursor.execute("SELECT path FROM images")

#image_paths = mycursor.fetchall()

#mycursor.execute("SELECT * FROM images")

#all_info = mycursor.fetchall()
#print(all_info)

create_table()


app = Flask(__name__)

@app.route("/")
def hello_world():
    #return render_template('index.html', image=image) 

    #############################################put back after testing
    #info = image_paths
    #return render_template('index.html',info = info,all_info= all_info )
    return render_template('index.html')




#mycursor = mydb.cursor()

#sql = "INSERT INTO images (name, path) VALUES (%s, %s)"
#val = ("Art 1", r"C:\Users\pauli\Documents\GitHub\Image_Repo\images\image.png")
#mycursor.execute(sql, val)

#mydb.commit()

#print(mycursor.rowcount, "record inserted.")

