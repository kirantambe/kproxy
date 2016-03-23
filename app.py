# -*- coding: utf-8 -*-
    
from flask import Flask, Response, render_template, stream_with_context, request

import requests

app = Flask(__name__)

def generate_response(url):	
		req = requests.get(url)
		return Response(req.content, content_type = req.headers['content-type'])

@app.route('/<path:url>')
def kprx(url):
	if not url.startswith('https://') and not url.startswith('https://'):
		url = 'http://' + url
	return generate_response(url)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		url = request.form['inpurl']
		return generate_response(url)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)