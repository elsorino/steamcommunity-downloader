# steamcommunity-downloader
Download various things from steam community

Script I made while learning Python

### Requirements

* Python3
  * BeautifulSoup4
  * Requests

### Usage

For steam comments, do:

`./stcommunity.py --comments -u https://steamcommunity.com/id/ChetFaliszek/ -n 2 -o example.txt`

This also supports group urls for group comments.

For group announcements, replace `--comments` with `--announcements`

Optionally, use `--html` to enable html output for steam emotes & profile links of commenters. 

Profiles must be public(for now)

TODO:

* Support private profiles
* Improve format of HTML output with auto resolving of vanity URLs
* Support more steam group stuff incl. events,  comments on announcements, discussions, hidden announcements
