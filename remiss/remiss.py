import flask
import json
import os
import pprint
import urllib.parse
import urllib.request

SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

app = flask.Flask(__name__)

@app.route('/')
def index():
    url = 'https://slack.com/api/team.info'
    params = {'token': SLACK_TOKEN}
    data = urllib.parse.urlencode(params).encode()
    response = urllib.request.urlopen(url, data=data)
    body = response.read().decode()
    j = json.loads(body)
    team_name = j['team']['name']
    team_icon = j['team']['icon']['image_132]
    return flask.render_template('index.html', slack_friendly_name=team_name)

@app.route('/invite', methods=['POST'])
def invite():
    email = flask.request.form['email']
    url = 'https://slack.com/api/users.admin.invite'
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
