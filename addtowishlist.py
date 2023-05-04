from flask import Flask, request,jsonify
from flask_cors import cross_origin
import pymongo

# app = Flask(__name__)

# @app.route('/addtowishlist',methods=['POST'])
# @cross_origin()
def addtowishlist():
    client = pymongo.MongoClient("mongodb+srv://tiwaryaakash00:a21815943289@cluster0.lgrv18e.mongodb.net/?retryWrites=true&w=majority")
    db = client['shopbuddy']
    collection = db['users']
    email = request.json['email']
    searchString = request.json['searchString']

    collection.update_one({"email":email},
                          { "$push" : {"wishlist":searchString}}
                    )
    
    data = collection.find_one({'email':email})
    del data["_id"]
    # print(data)
    
    return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)

