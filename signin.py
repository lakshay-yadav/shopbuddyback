from flask import Flask, request,jsonify
from flask_cors import cross_origin
import pymongo
import json
# app = Flask(__name__)

# @app.route('/signin',methods=['POST'])
# @cross_origin()
def signin():
    # mongodb://localhost:27017/
    # 
    client = pymongo.MongoClient("mongodb+srv://tiwaryaakash00:a21815943289@cluster0.lgrv18e.mongodb.net/?retryWrites=true&w=majority")
    db = client['shopbuddy']
    collection = db['users']
    email = request.json['email']
    password = request.json['password']

    if collection.count_documents({'email':email}) == 0:
        return jsonify({"status":"Email not found"})
    
    else:
     if collection.count_documents({'email':email,'password':password})==0:
            return jsonify({"status":"Wrong email password combination"})
     else:
           data = collection.find_one({'email':email})
           del data["_id"]
           print(data)
           return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

