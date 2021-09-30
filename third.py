import urllib.request
import mysql.connector
import os

# connect to db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraper-olx"
)
mycursor = mydb.cursor()

# get from db function
def getDB(mycursor):
    sql = "SELECT * FROM images"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result

data = getDB(mycursor)

for x in data:

    folder = './' + str(x[1])
    isExist = os.path.exists(folder)

    if not isExist:
        os.makedirs(folder)

    urllib.request.urlretrieve(x[2], folder+"/"+str(x[0])+"_"+str(x[1])+".jpeg")