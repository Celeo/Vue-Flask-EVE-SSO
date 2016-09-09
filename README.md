# Vue-Flask-EVE-SSO

This is an example web app to demonstrate one approach to the EVE SSO authentication flow through CREST using Vue.js on the frontend and Flask (Python) on the backend.

## Setup

1. Install Node and npm
2. `git clone https://github.com/Celeo/Vue-Flask-EVE-SSO`
3. `cd Vue-Flask-EVE-SSO/front`
4. `npm install`
5. `cd ../back`
6. `virtualenv env`
7. `. env/bin/activate`
8. `pip install -r requirements.txt`
9. Copy both example configurations to new files without the `.extension` string and supply the configuration. The secret key must match between frontend and backend, and you must have a EVE Developer Application setup on https://developers.eveonline.com to complete the backend configuration.

## Running

### Development

For development, use the provided dev servers for both components:

1. `cd front && npm run dev`
3. In another terminal window, `cd back && . env/bin/activate && export FLASK_APP=app.py && flask run`

### Production

This app doesn't do anything beyond log someone in, but if you *were* going to run in a production-like environment:

1. Build the compact frontend app with `cd front && npm run build`
2. Configure your webserver (Nginx, etc.) to point to `index.html`
3. Run the Flask app with Gunicorn, uWSGI, etc.
