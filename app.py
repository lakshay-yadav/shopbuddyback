from flask import Flask
from flask_cors import cross_origin
import signup
import signin
import flipkart
import website
import category
import specs

app = Flask(__name__)

@app.route('/specs',methods=['POST'])
@cross_origin()
def specsscrap():
    return specs.specs()

@app.route('/category',methods=['POST'])
@cross_origin()
def categoryscrap():
    return category.category()

@app.route('/website',methods=['POST'])
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
