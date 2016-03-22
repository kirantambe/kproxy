# -*- coding: utf-8 -*-
    
from flask import Flask, Response, render_template, stream_with_context

import requests

app = Flask(__name__)

@app.route('/<path:url>')
def kprx(url):
	if not url.startswith('https://') and not url.startswith('https://'):
		url = 'http://' + url
	req = requests.get(url, stream=True)
	return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)