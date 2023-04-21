from flask import Flask, request,jsonify
from flask_cors import cross_origin
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/flipkart',methods=['POST'])
@cross_origin()
def flipkart():
    searchString = request.json['searchString'].replace(" ","")
    flipkart_url = "https://www.flipkart.com/search?q=" + searchString
    r = requests.get(flipkart_url)
    flipkart_html = bs(r.content,"html5lib")
    content = flipkart_html.findAll("div",{"class":"_13oc-S"})
    lis = []
    for d in content:
        try:
            src = d.div.div.div.div.div.div.img['src']
            name = d.div.div.div.next_sibling.div.div.string
            rating = d.div.div.div.next_sibling.div.div.next_sibling.span.div.text
            price = d.div.div.div.next_sibling.div.next_sibling.div.div.div.string
        except:
            pass 
        
        dict = {"price":price,"rating":rating,"name":name,"src":src}
        lis.append(dict)
    return (jsonify(lis))

if __name__ == '__main__':
    app.run(debug = True)
