#!/usr/bin/env python3
import requests
import re
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help = "URL of steam profile or group to use")
parser.add_argument("-n", "--numbers", required=True, help = "Number of comment pages to download")
parser.add_argument("-o", "--output", required=True, help = "File to direct output")
parser.add_argument("--html", action='store_true', help = "Enables HTML output for emotes/urls")
args = parser.parse_args()
url = args.url

if "steamcommunity" in url:
    url +="/allcomments?ctp="
else:
    print("\nInvalid url entered, exiting")
    quit()

pagenumbers = int(args.numbers)
currentnumber = 1 #Start with first page

while currentnumber <= pagenumbers:
    currentpage = url + str(currentnumber)
    page = requests.get(currentpage)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find('div', class_='commentthread_comment_container') #Where all comments are located
    if args.html:
        print(results, file=open(args.output,"a+", encoding='utf-8')) #utf-8 encoding is required on windows
        currentnumber += 1
    else:
        finaltext = re.sub(r'([\r\n\t])+', r'\n', results.text) #Removes a bunch of blank lines
        print(finaltext.strip(), file=open(args.output,"a+", encoding='utf-8')) 
        currentnumber += 1