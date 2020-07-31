#Build a python script that can fetch news headlines from https://www.hindustantimes.com/ homepage

#To build this python script we use Beautifulsoup4
import bs4
import requests

url = "http://hindustantimes.com"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')

#It will find all the headlines of newpaper feed

for headlines in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
    print(headlines.text)


