# import the necessary libraries
from bs4 import BeautifulSoup
import requests
import mysql.connector

# specify the URL of the website you want to scrape
url = 'https://www.coingecko.com/'

# send a GET request to the website and retrieve the HTML
response = requests.get(url)
html = response.text

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# extract the data from the website
data = soup.find_all('div', {'class': 'coin-summary-item'})

# create a list to store the extracted data
coin_data = []

# loop through the data and extract the relevant information
for item in data:
    name = item.find('h3').text
    price = item.find('h4').text
    market_cap = item.find('p', {'class': 'market-cap'}).text
    volume = item.find('p', {'class': 'volume'}).text

    # store the data in a dictionary
    coin = {
        'name': name,
        'price': price,
        'market_cap': market_cap,
        'volume': volume
    }

    # add the dictionary to the list
    coin_data.append(coin)

# connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname', database='database_name')

# create a cursor object
cursor = cnx.cursor()

# loop through the list of data and insert it into the database
for item in coin_data:
    query = 'INSERT INTO coin_prices (name, price, market_cap, 24h_volume) VALUES (%s, %s, %s, %s)'
    values = (item['name'], item['price'], item['market_cap'], item['volume'])
    cursor.execute(query, values)

# commit the changes to the database
cnx.commit()

# close the cursor and connection
cursor.close()
cnx.close()
