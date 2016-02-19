import flask
import os

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
    return 'This is the part where I send an invitation to {}.'.format(email)

def main():
    app.run()

if __name__ == '__main__':
    main()
