import requests
from bs4 import BeautifulSoup
import re

url = input("Please paste comment url, example: https://steamcommunity.com/id/sargentyen/allcomments\n")
allcomments = "allcomments"
if "allcomments" in url:
    pass
else:
    print("\nInvalid url entered, exiting")
    quit()

pagenumbers = int(input("How many pages of comments would you like to download?\n"))

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find('div', class_='maincontent') #Where all comments are located
steam_elems = results.find_all('div', class_='commentthread_comments') #Finds all comments

for all in steam_elems:
    test = re.sub(r'([\r\n\t])+', r'\n', all.text) #Removes a bunch of blank lines
    print(test)

