# -*- coding: utf-8 -*-
    
from flask import Flask, Response, render_template, stream_with_context, request

import requests

app = Flask(__name__)

@app.route('/<path:url>')
def kprx(url):
	if not url.startswith('https://') and not url.startswith('https://'):
		url = 'http://' + url
	req = requests.get(url, stream=True)
	return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		url = request.form['inpurl']
		req = requests.get(url, stream=True)
		return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])
	return render_template('index.html')

if __name__ == '__main__':
	app.run(debug=True)