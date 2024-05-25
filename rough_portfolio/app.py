#!/usr/bin/python3
from flask import Flask, jsonify, send_from_directory
import random
import string
import threading
import time
import os

app = Flask(__name__, static_folder='stylesheets')

current_code = None

def generate_code():
    global current_code
    while True:
        current_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        time.sleep(60)

@app.route('/generate_code')
def get_code():
    return jsonify(code=current_code)

@app.route('/')
def index():
    return send_from_directory('pages', 'index.html')

@app.route('/stylesheets/<path:path>')
def send_css(path):
    return send_from_directory('stylesheets', path)

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

if __name__ == '__main__':
    code_thread = threading.Thread(target=generate_code)
    code_thread.daemon = True
    code_thread.start()
    app.run(debug=True)