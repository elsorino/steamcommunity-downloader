# steam-comments
Imports comments from a user's steam profile

Script I made while learning Python

### Requirements

* Python3
  * BeautifulSoup4
  * Requests

### Usage

`./steam-comments.py -p https://steamcommunity.com/id/ChetFaliszek/allcomments -n 2 -o example.txt`

Profile must be public(for now)

TODO:

* Support private profiles
* Support steam group comments
* Support steam emotes. Currently emotes are blanked out
