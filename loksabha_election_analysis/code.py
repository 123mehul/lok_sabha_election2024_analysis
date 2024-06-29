from bs4 import BeautifulSoup
import requests

url= 'https://results.eci.gov.in/'
page= requests.get(url)
soup=BeautifulSoup(page.text,'html')
print(soup)