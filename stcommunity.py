#!/usr/bin/env python3
import requests
import re
import argparse
from bs4 import BeautifulSoup
from steam.steamid import SteamID

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
stcss = """
<head>
	<style type="text/css">
	
html {
	height: 100%;
}

body {
	background:  #1b2838;
	text-align: left;
	color: #8F98A0;
	font-size: 14px;
	margin:0;
	padding:0;
}

body {
	font-family:Arial, Helvetica, Verdana, sans-serif;
}

a {
	color: #ebebeb;
	text-decoration: none;
	cursor: pointer;
}

.commentthread_comment_container {
	margin-top: 19px;
}

.commentthread_comment {
	position: relative;
	padding-bottom: 8px;
	padding-top: 8px;
	margin-bottom: 8px;
	min-height: 40px;
	padding-left: 58px;
	overflow: hidden;
}

.commentthread_comment_avatar {
	position: absolute;
	left: 5px;
	top: 8px;
}


.commentthread_comment_text {
	font-size: 13px;
	color: #acb2b8;
	word-wrap: break-word;
	overflow-y: auto;	
}

img.emoticon {
	vertical-align: text-bottom;
	height: 18px;
	width: 18px;
}

	</style>
</head>
"""
if args.html:
    print(stcss, file=open(args.output,"a+", encoding='utf-8'))

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
        print("Downloading page",currentnumber)
        page = requests.get(currentpage)
        soup = BeautifulSoup(page.content, 'html.parser')
        comresults = soup.find('div', class_='commentthread_comment_container') #Where all comments are located
        if args.html:
            output_lines = [] #Gotta reset the list on every page
            urls = re.findall('https:\/\/steamcommunity\.com\/id\/[a-zA-Z0-9]+', str(comresults))
            #The following is very inefficent, it has no duplication detection.
            for found in urls:
                #print(found)
                id64 = SteamID.from_url(found)
                #print(id64)
                urlf = re.sub(r'id\/[a-zA-Z0-9]+', r'profiles/%s' % id64, found, re.MULTILINE)
                #print(urlf)
                output_lines.append(urlf)
            test = re.sub('https://steamcommunity.com\/id\/[a-zA-Z0-9]+', lambda _: output_lines.pop(0), str(comresults), len(output_lines) or -1)
            print(test.strip(), file=open(args.output,"a+", encoding='utf-8')) 
            currentnumber += 1
        else:
            finaltext = re.sub(r'([\r\n\t])+', r'\n', comresults.text) 
            print(finaltext.strip(), file=open(args.output,"a+", encoding='utf-8')) 
            currentnumber += 1