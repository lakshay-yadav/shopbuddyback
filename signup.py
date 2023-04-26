from flask import Flask, request,jsonify
from flask_cors import cross_origin
import pymongo

app = Flask(__name__)

@app.route('/signup',methods=['POST'])
@cross_origin()
def signup():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['shopbuddy']
    collection = db['users']
    name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    if collection.count_documents({'email':email}) == 0:
        dic = {"name":name,"email":email,"password":password,"wishlist":[]}
        collection.insert_one(dic)
    
    else:
        return jsonify({"status":"Email already exist"})

    return jsonify({"status":"Ok"})

if __name__ == '__main__':
    app.run(debug= True)
