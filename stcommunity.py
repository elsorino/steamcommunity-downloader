#!/usr/bin/env python3
import requests
import re
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", required=True, help = "URL of steam profile or group to use")
parser.add_argument("-n", "--numbers", required=True, help = "Number of comment pages to download")
parser.add_argument("-o", "--output", required=True, help = "File to direct output")
parser.add_argument( "--html", action='store_true', help = "Enables HTML output for emotes/urls")
parser.add_argument("--announcements", action='store_true', help = "Download announcements on a steam group")
args = parser.parse_args()
url = args.url

pagenumbers = int(args.numbers)
currentnumber = 1 #Start with first page

if args.announcements:
    if "steamcommunity.com/groups/" in url:
        url +="/announcements/listing?p="
    else:
        print("\nInvalid url entered, exiting")
        quit()
    while currentnumber <= pagenumbers:
        currentpage = url + str(currentnumber)
        page = requests.get(currentpage)
        soup = BeautifulSoup(page.content, 'html.parser')
        announceresults = soup.find_all('div', class_='announcement') #Preferred not to use find_all, but there was no better way
        if args.html:
            for all in announceresults:
                print(all, file=open(args.output,"a+", encoding='utf-8')) #utf-8 encoding is required on windows
                currentnumber += 1
        else:
            for all in announceresults:
                test = re.sub(r'([\r\n\t])+', r'\n', all.text) #Removes a bunch of blank lines
                print(test.strip(), file=open(args.output,"a+", encoding='utf-8'))
            currentnumber += 1
else:
    if "steamcommunity.com/id/" in url:
        url +="/allcomments?ctp="
    else:
        print("\nInvalid url entered, exiting")
        quit()
    while currentnumber <= pagenumbers:
        currentpage = url + str(currentnumber)
        page = requests.get(currentpage)
        soup = BeautifulSoup(page.content, 'html.parser')
        comresults = soup.find('div', class_='commentthread_comment_container') #Where all comments are located
        if args.html:
            print(comresults, file=open(args.output,"a+", encoding='utf-8'))
            currentnumber += 1
        else:
            finaltext = re.sub(r'([\r\n\t])+', r'\n', comresults.text) 
            print(finaltext.strip(), file=open(args.output,"a+", encoding='utf-8')) 
            currentnumber += 1