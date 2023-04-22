from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq
import signup
import signin
import flipkart
import website

app = Flask(__name__)

@app.route('/webiste',methods=['POST'])
@cross_origin()
def websitescrap():
    return website.website()

@app.route('/signup',methods=['POST'])
@cross_origin()
def signuproute():
    return signup.signup()

@app.route('/signin',methods=['POST'])
@cross_origin()
def signinroute():
    return signin.signin()

@app.route('/flipkart',methods=['POST'])
@cross_origin()
def flipkartscrap():
    return flipkart.flipkart()

if __name__ == '__main__':
    app.run(debug=True)