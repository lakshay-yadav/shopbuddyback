from flask import Flask, request,jsonify
from flask_cors import cross_origin
import requests
from bs4 import BeautifulSoup as bs

# app = Flask(__name__)

# @app.route('/flipkartreviews',methods=['POST'])
# @cross_origin()
def flipkartreviews():
    searchString = request.json['searchString'].replace(" ","")
    flipkart_url = "https://www.flipkart.com/search?q=" + searchString

    r = requests.get(flipkart_url)
    flipkart_html = bs(r.content,"html5lib")

    content = flipkart_html.findAll("div",{"class":"_13oc-S"})
    link = "https://www.flipkart.com" + content[0].div.div.a['href']

    newPage = requests.get(link)
    newPage_html = bs(newPage.content,"html5lib")
    
    content = newPage_html.findAll("div",{"class":"_16PBlm"})

    lis = []

    for d in content[0:3]:
        rating = d.div.div.div.div.text
        shortreview = d.div.div.div.p.text
        longreview = d.div.div.div.next_sibling.div.div.div.text

        dic = {"rating":rating,"shortreview":shortreview,"longreview":longreview}

        lis.append(dic)
    
    link = "https://www.flipkart.com" + newPage_html.findAll("div",{"class":"col JOpGWq"})[0].a['href']

    dic = {"link":link}

    lis.append(dic)
    
    return jsonify(lis)

# if __name__ == '__main__':
#     app.run(debug = True)

