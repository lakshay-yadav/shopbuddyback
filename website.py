from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/website',methods=['POST'])
@cross_origin()
def website():
    print("inside this function")
    searchString = request.json['searchString'].replace(" ","-")
    site_url = "https://www.pricedekho.com/mobiles/" + searchString + "-price-mp.html"
    # site_url = "https://www.pricedekho.com/mobiles/apple-iphone-11-price-mp.html"
    # print("########")
    # print(site_url)
    r = requests.get(site_url)
    site_html = bs(r.content,"html5lib")
    content = site_html("table",{"class":"allvariant contentHold"})

    tbody = content[0].findAll('tbody')
    tr = tbody[0].findAll('tr')

    lis = []

    for d in tr:
        try:
            src = d.td.img['src']
            price = d.td.next_sibling.text
            link = d.td.next_sibling.next_sibling.a['href']

        except Exception as e:
            print("The exception is ", e)
            return 'Something is wrong'
        
        dic = {"src":src,"price":price,"link":link}
        lis.append(dic)
    return jsonify(lis)

if __name__ == "__main__":
    app.run(debug=True)
