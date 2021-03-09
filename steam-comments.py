#!/usr/bin/env python3
import requests
import re
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--profile", required=True, help = "Comment url of steam profile to use")
parser.add_argument("-n", "--numbers", required=True, help = "Number of comment pages to use")
parser.add_argument("-o", "--output", required=True, help = "File to direct output")
args = parser.parse_args()
url = args.profile

if "allcomments" in url:
    pass
else:
    print("\nInvalid url entered, exiting")
    quit()

url +="?ctp=" #Needed for page numbers

pagenumbers = int(args.numbers)
currentnumber = 1 #Start with first page

while currentnumber <= pagenumbers:
    currentpage = url + str(currentnumber)
    page = requests.get(currentpage)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='maincontent') #Where all comments are located
    steam_elems = results.find_all('div', class_='commentthread_comments') #Finds all comments

    for all in steam_elems:
        test = re.sub(r'([\r\n\t])+', r'\n', all.text) #Removes a bunch of blank lines
        print(test.strip(), file=open(args.output,"a+", encoding='utf-8')) #utf-8 encoding is required on windows
    currentnumber += 1