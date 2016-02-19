import flask
import os

SLACK_TEAM_NAME = os.environ.get('SLACK_TEAM_NAME')
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')

app = flask.Flask(__name__)

@app.route('/')
def index():
    if SLACK_TEAM_NAME is None:
        return 'You need to set the \'SLACK_TEAM_NAME\' environment variable.'
    if SLACK_TOKEN is None:
        return 'You need to set the \'SLACK_TOKEN\' environment variable.'
    return 'This is where you put your email address.'

@app.route('/invite', methods=['POST'])
def invite():
    email = flask.request.form['email']
    return 'This is the part where I send an invitation to {}.'.format(email)

def main():
    app.run()

if __name__ == '__main__':
    main()
