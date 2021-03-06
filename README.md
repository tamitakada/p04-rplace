# My Space by TilesStyle

## Roster
- Liesel Wong: Routing, Websockets  
- Shyne Choi: Sass/CSS, JS, Websockets  
- Emma Buller: Sass/CSS, JS, Websockets, Droplet  
- Tami Takada: PM, Database, Websockets, Droplet  

## Description
My Space is a replica of [r/place](https://www.reddit.com/r/place/) but with a 10 second timer (for easier demo). It's a place for users to work together or against each other on a collaborative art canvas where. There exists a 10 second timer for limiting a single user or group of users from dominating the whole canvas, allowing everyone to be a part of the artwork.

## Launch Codes
FULL EXPERIENCE:  

Install and run My Space on your own machine:

1. Run `git clone git@github.com:tamitakada/p04-rplace.git`
2. Enter the cloned directory with `cd p04-rplace`
3. Create a virtual environment and install required pip modules
```
python3 -m venv venv
. venv/bin/activate
pip3 install -r requirements.txt
```
4. Run the app with `python3 myspace/__init__.py`
5. Visit http://localhost:8000/ to view the app

OR  

To view our live app, visit http://142.93.124.70/  
NOTE: Unfortunately, the socket code doesn't seem to work on the live app, so you have to refresh the home page to see canvas updates. However, other than that, the app runs just like it does when installed locally.
