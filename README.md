# steamcommunity-downloader
Export things such as comments from Steam community

Script I made while learning Python

### Requirements

* Python3
  * BeautifulSoup4
  * Requests
  * SteamID

### Usage

For steam comments, do:

`./stcommunity.py -u https://steamcommunity.com/id/ChetFaliszek/ -n 2 -o example.txt`

This also supports group urls for group comments.

For group announcements, use `--announcements`

Optionally, use `--html` to enable html output for steam emotes & profile links.

Profiles must be public(for now)

This does however, work on community banned profiles.

TODO:

* Support private profiles
* Support more steam group stuff incl. events,  comments on announcements, discussions, hidden announcements
