import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import mysql.connector

# connects to db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="scraper-olx"
)
mycursor = mydb.cursor()

# link fetcher
http = httplib2.Http()

# save to db function
def saveDB(link, mycursor):

    # Checks if data is already available or not
    val = link
    sql = "SELECT * FROM links where link = (%s)"
    mycursor.execute(sql, (val,))
    lenght = mycursor.fetchall()

    if len(lenght) == 0:
        # Inserts into DB
        sql = "INSERT INTO links (link) VALUES (%s)"
        mycursor.execute(sql, (val,))
        mydb.commit()


i = 0
while i <= 49:

    # fetches 49 pages
    if i == 0:
        url = 'https://www.olx.com.pk/cars_c84'
    else:
        url = 'https://www.olx.com.pk/cars_c84?page=' + str(i)

    # fetches data from link
    status, response = http.request(url)

    # link gets inventory data and saves to db
    for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
        if link.has_attr('href'):
            if '/item/' in link['href']:
                saveDB(link['href'], mycursor)

    i += 1
