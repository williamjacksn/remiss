import flask
import json
import os
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
    team_icon = j['team']['icon']['image_132']
    return flask.render_template('index.html', team_name=team_name,
                                 team_icon=team_icon)


@app.route('/invite', methods=['POST'])
def invite():
    url = 'https://slack.com/api/users.admin.invite'
    email = flask.request.form['email']
    params = {'email': email, 'token': SLACK_TOKEN, 'set_active': 'true'}
    data = urllib.parse.urlencode(params).encode()
    response = urllib.request.urlopen(url, data=data)
    body = response.read().decode()
    j = json.loads(body)
    if j['ok']:
        return flask.render_template('success.html', j=j)
    return flask.render_template('failure.html',  j=j)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
