import os
from flask import Flask, jsonify, request
import requests
import my_keys
import ast
app = Flask(__name__)
#app.debug = True

## make sure to add your cx and api keys, i put mine in a file named my_keys (hidden)

@app.route('/')
def hello():
	return 'Hello World!!'

@app.route('/image', methods=['POST'])
def returnJson():
	#make json
	request_data = request.form.get('text')
	imageUrl = getImage(request_data)
	#return it
	return jsonify(response_type='in_channel',text=imageUrl)

@app.route('/math', methods=['POST'])
def doMath():
	#get data from the post, evaluate it, and return JSON
	requestData = request.form.get('text')
	#literalEval because it's very limited in what it will accept
	mathResult = ast.literalEval(requestData)
	return jsonify(response_type='in_channel',text=mathResult)


def getImage(request_data):
	url = 'https://www.googleapis.com/customsearch/v1?q=' + request_data + '&cx=' + my_keys.cx + '&safe=medium&searchType=image&key=' + my_keys.api_key
	goog_search = requests.get(url)
	response = goog_search.json()
	first_image_url = response['items'][0]['link']
	return first_image_url

# only for testing
#app.run()