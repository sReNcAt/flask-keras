from flask import Flask, request, render_template, jsonify, session, redirect, url_for
from werkzeug import secure_filename

import os

import controller as ctr

app = Flask(__name__) 

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/') 
def index():
    return ctr.index()

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    try :
        return ctr.upload(request.method,request.files['file'])
    except Exception as e:
        return ctr.upload(request.method,'err')

@app.errorhandler(500)
def internal_error(error):
    return ctr.internalerror("시스템이 오류를 발생햇졍 ㅠ")

if __name__ == '__main__': 
    app.run('127.0.0.1', debug=False)