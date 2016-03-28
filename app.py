# -*- coding: utf-8 -*-
    
from flask import Flask, Response, render_template, stream_with_context, request

import requests

app = Flask(__name__)

def generate_response(url):
	if not url.startswith('https://') and not url.startswith('http://'):
		url = 'http://' + url
	req = requests.get(url, stream=True)
	return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

@app.route('/<path:url>')
def kprx(url):
	return generate_response(url)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		url = request.form['inpurl']
		return generate_response(url)
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)