import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'This is the index.'

def main():
    app.run()

if __name__ == '__main__':
    main()
