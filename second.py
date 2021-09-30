import mysql.connector
import requests
import re
import json

# connect to db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraper-olx"
)
mycursor = mydb.cursor()

# save to db function
def saveDB(data, mycursor, url):
    sql = '''INSERT INTO `car_inventory`(`url`, `description`, `make`, `model`, `new_used`, `petrol`, 
    `mileage`, `registration_city`, `year`, `country`, `city`, `state`, `area`, `title`, `price`) VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    description = data['description'].replace(r'[redacted phone number]', '')
    values = (url, description, data['extraFields']['make'], data['extraFields']['model'],
              data['extraFields']['new_used'], data['extraFields']['petrol'], data['extraFields']['mileage'],
              data['extraFields']['registration_city'], data['extraFields']['year'], data['location'][0]['name'],
              data['location'][1]['name'], data['location'][2]['name'], data['location'][3]['name'], data['title'],
              data['extraFields']['price'])

    mycursor.execute(sql, values)
    mydb.commit()

    insertId = mycursor.lastrowid

    for x in data['photos']:
        sql = 'INSERT INTO `images`(`inv_id`, `url`) VALUES (%s, %s)'
        values = (insertId, x['url'])
        mycursor.execute(sql, values)
        mydb.commit()


# get from db function
def getDB(mycursor):
    sql = "SELECT DISTINCT(link) FROM links"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


data = getDB(mycursor)
for x in data:

    # url concat
    url = 'https://www.olx.com.pk' + x[0]
    # fetches data from link
    html = requests.get(url).text
    # fetches state var
    data = re.findall(r'window.state = .*}}', html)
    if len(data) != 0:
        data = str(data[0])
        # removes useless data
        data = data.replace('window.state = ', '')
        # converts it into json
        data = json.loads(data)
        # gets required result
        data = data['ad']['data']
        # save data to db
        saveDB(data, mycursor, x[0])
