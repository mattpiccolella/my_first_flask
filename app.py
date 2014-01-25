from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Pushing from my local machine...'

if __name__ == '__main__':
    app.run()
