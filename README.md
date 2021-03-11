# steam-comments
Imports comments from a user's steam profile

Script I made while learning Python

### Requirements

* Python3
  * BeautifulSoup4
  * Requests

### Usage

`./steam-comments.py -u https://steamcommunity.com/id/ChetFaliszek/ -n 2 -o example.txt`

Optionally, use `--html` to enable html output for steam emotes & profile links of commenters 

Profile must be public(for now)

TODO:

* Support private profiles
* Improve format of HTML output with auto resolving of vanity URLs
