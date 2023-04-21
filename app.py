from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/product',methods=['GET','POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ","-")
            site_url = "https://pricee.com/?q=" + searchString
            uClient = uReq(site_url)
            sitePage = uClient.read()
            uClient.close()
            site_html = bs(sitePage, "html.parser")
            

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)