from flask import Flask,request,jsonify
from flask_cors import cross_origin
import requests
from bs4 import BeautifulSoup as bs

# app = Flask(__name__)

# @app.route('/specs',methods=['POST'])
# @cross_origin()
def specs():
    searchString = request.json['searchString'].replace(" ","")
    flipkart_url = "https://www.flipkart.com/search?q=" + searchString
    r = requests.get(flipkart_url)
    flipkart_html = bs(r.content,"html5lib")
    content = flipkart_html.findAll("div",{"class":"_13oc-S"})
    link = "https://www.flipkart.com" + content[0].div.div.a['href']

    newPage = requests.get(link)
    newPage_html = bs(newPage.content,"html5lib")
    
    content = newPage_html.findAll("table",{"class":"_14cfVK"})
    # print(content)
    # print(len(content))
    lis = []

    for d in content:
        newContent = d.findAll("tr",{"class":"_1s_Smc row"})
        # print(newContent)
        # print(len(newContent))

        dic = {}
        for n in newContent:
            try :
                keyName = n.td.text
                valueName = n.td.next_sibling.ul.li.text
                dic[keyName] = valueName
            except:
                pass
            
        lis.append(dic)
    return jsonify(lis)
    
# if __name__ == '__main__':
#     app.run(debug = True)

