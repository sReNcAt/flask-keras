from flask import Flask, request, render_template, jsonify, session, redirect, url_for,Markup
from werkzeug import secure_filename

import process # process.py
import base64
import uuid
import os

from web import allowed_file

def index():
    print("Hello")
    return render_template('index.html',text='Hello, World!')

def upload(method,file):
    try :
        if(method=='POST'):
            if(file=='err'):
                raise Exception('다시 시도하여 주세요.')
            if(file==''):
                raise Exception('파일이 비었습니다.')
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join('uploads/', filename))
                rt = process.aa(filename)
                return render_template('index.html',text=rt,uploadfiled=False)

        else:
            return render_template('index.html',text='개, 고양이 사진을 올려주세요.')
    except Exception as e :
        print(e)
        return render_template('index.html',text='에러 발생')
    except :
        return render_template('index.html',text='에러 발생')
    
def internalerror(e):
    return render_template('index.html',text='에러 발생',uploadfiled=False)