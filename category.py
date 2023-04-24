from flask import Flask,request,jsonify
from flask_cors import cross_origin
import requests
from bs4 import BeautifulSoup as bs

# app = Flask(__name__)

# @app.route('/category',methods=['POST'])
# @cross_origin()
def category():
    searchString = request.json['searchString'].replace(" ","")
    flipkart_url = "https://www.flipkart.com/search?q=" + searchString
    r = requests.get(flipkart_url)
    flipkart_html = bs(r.content,"html5lib")
    content = flipkart_html.findAll("div",{"class":"_13oc-S"})
    link = "https://www.flipkart.com" + content[0].div.div.a['href']

    newPage = requests.get(link)
    newPage_html = bs(newPage.content,"html5lib")
    
    # print(content)
    # print(len(content))
    category = newPage_html.findAll("div",{"class":"_3k-BhJ"})
    dic = {}
    count  = 1
    for d in category:
        dic[count] = d.div.text
        count = count+1
    
    lis = []
    lis.append(dic)
    return jsonify(lis)


# if __name__ == '__main__':
#     app.run(debug = True)

