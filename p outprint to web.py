
from pywebio.input import *
from pywebio.output import put_text
from pywebio import session

#dependencies

import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlencode

#list of URLs
urls = [

   'https://www.investing.com/equities/nike',

   'https://www.investing.com/equities/coca-cola-co',

   'https://www.investing.com/equities/microsoft-corp',

]

#starting our CSV file
file = open('stockprices.csv', 'w')

writer = csv.writer(file)

writer.writerow(['Company', 'Price', 'Change'])

#looping through our list

for url in urls:

   #sending our request through ScraperAPI

   params = {'api_key': '51e43be283e4db2a5afb62660fc6ee44', 'url': url}

   page = requests.get('http://api.scraperapi.com/', params=urlencode(params))

   #our parser

   soup = BeautifulSoup(page.text, 'html.parser')

   company = soup.find('h1', {'class': 'text-2xl font-semibold instrument-header_title__GTWDv mobile:mb-2'}).text

   price = soup.find('div', {'class': 'instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold'}).find_all('span')[0].text

   change = soup.find('div', {'class': 'instrument-price_instrument-price__3uw25 flex items-end flex-wrap font-bold'}).find_all('span')[2].text

   #printing to have some visual feedback

   print('Loading :', url)

   print(company, price, change)
   
   put_text('Loading :', url)
   put_text(company, price, change)

   #writing the data into our CSV file

   writer.writerow([company.encode('utf-8'), price.encode('utf-8'), change.encode('utf-8')])

file.close()

# put_text('Loading :', url)
# put_text(company, price, change)

session.hold()