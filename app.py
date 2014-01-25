from flask import Flask, jsonify
from flask import render_template
import requests

app = Flask(__name__)
def parse_response(response_dict):
    cleaned_response = {}
    cleaned_response['total_count'] = response_dict['total_count']
    cleaned_response['items'] = []
    for a in response_dict['items']:
        new_dict = {'name':a['name'],'owner':{'login':a['owner']['login'],'avatar_url':a['owner']['avatar_url'], 'html_url':a['owner']['html_url']}, 'html_url':a['html_url'], 'description':a['description']}
        cleaned_response['items'].append(new_dict)
    return cleaned_response

@app.route('/')
def hello_world():
    return 'Pushing from my local machine...'

@app.route('/users/<username>')
def user_pages(username):
    return 'User %s' % username

@app.route('/home')
@app.route('/home/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(404)
def internal_server_error(error):
    return render_template('500.html'), 500

@app.route('/search/<search_query>')
def search(search_query):
    url = "https://api.github.com/search/repositories?q=" + search_query
    response_dict = requests.get(url).json()    
    cleaned_response = parse_response(response_dict)
    return render_template('search.html', api_data=cleaned_response)
    
if __name__ == '__main__':
    app.debug = True
    app.run()
