import flask
import json
import os
import urllib.parse
import urllib.request

SLACK_FRIENDLY_NAME = os.environ.get('SLACK_FRIENDLY_NAME')
SLACK_SUBDOMAIN = os.environ.get('SLACK_SUBDOMAIN')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html', slack_friendly_name=SLACK_FRIENDLY_NAME)

@app.route('/invite', methods=['POST'])
def invite():
    email = flask.request.form['email']
    url = 'https://{}.slack.com/api/users.admin.invite'.format(SLACK_SUBDOMAIN)
    params = {'email': email, 'token': SLACK_TOKEN, 'set_active': 'true'}
    data = urllib.parse.urlencode(params).encode()
    response = urllib.request.urlopen(url, data=data)
    body = response.read().decode()
    j = json.loads(body)
    return json.dumps(j, indent=2, sort_keys=True)

def main():
    app.run()

if __name__ == '__main__':
    main()
