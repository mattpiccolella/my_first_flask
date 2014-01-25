from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World, this is Matt and I know Flask!'

if __name__ == '__main__':
    app.run()
