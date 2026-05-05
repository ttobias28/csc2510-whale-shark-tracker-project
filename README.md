# 🦈 Whale Shark Sighting Tracker

## What is this?
A web application that lets marine researchers and enthusiasts log and track 
whale shark sightings from around the world. Users can record where a whale 
shark was spotted, how big it was, who saw it, and any additional notes about 
the encounter. This is human-generated data, NO information pulled from online sources.

## Live App
http://34.134.126.68/

The Live App does not work at this moment, since the terraform-instance VM is currently NOT running. Consider one of the options below:

## Running Locally

### Option 1 — Plain Python
```bash
git clone https://github.com/ttobias28/csc2510-whale-shark-tracker-project.git
cd csc2510-whale-shark-tracker-project
pip install -r requirements.txt
python wsgi.py
```
Then open http://localhost:5000 in your browser.

### Option 2 — Docker
```bash
docker pull ttobias42/csc2510-whale-shark-tracker-project:latest
docker run -p 5000:5000 ttobias42/csc2510-whale-shark-tracker-project:latest
```
Then open http://localhost:5000 in your browser.
