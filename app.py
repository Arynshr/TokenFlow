from flask import Flask, render_template, request, jsonify
import os
import tokeniser

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    
