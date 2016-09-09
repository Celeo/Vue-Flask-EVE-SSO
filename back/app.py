from flask import Flask, request, jsonify
from preston.crest import Preston
from flask_cors import CORS
import jwt


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
preston = Preston(
    user_agent='EVE SSO Vue+Flask example, celeodor@gmail.com',
    client_id=app.config['EVE_OAUTH_CLIENT_ID'],
    client_secret=app.config['EVE_OAUTH_SECRET'],
    callback_url=app.config['EVE_OAUTH_CALLBACK']
)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Get the SSO authorize URL or process a login.

    This method, when accessed with a GET request returns the URL
    that a user needs to be sent to in order to start the EVE SSO
    process. When accessed with a POST request, this method
    expects the presence of the ``code`` payload key, which is then
    used by Preston to get the name of the character the user is
    authenticating with. This name is encrypted into a JWT and
    returned as a string to the client.

    Methods:
        GET
        POST

    Args:
        None

    Returns:
        str: JWT with the ``character_name`` key
    """
    if request.method == 'GET':
        return jsonify(url=preston.get_authorize_url())
    try:
        code = request.form['code']
        character_information = preston.authenticate(code).whoami()
        character_name = character_information['CharacterName']
        return jwt.encode({'character_name': character_name}, app.config['SECRET_KEY'], algorithm='HS256')
    except Exception:
        return jsonify({'message': 'An error was returned by CREST when getting character information'}), 500
