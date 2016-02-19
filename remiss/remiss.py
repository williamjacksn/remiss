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
    return 'https://{}.slack.com/api/users.admin.invite'.format(SLACK_TEAM_NAME)

def main():
    app.run()

if __name__ == '__main__':
    main()
