from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs

# app = Flask(__name__)

# @app.route('/amazon',methods=['POST'])
# @cross_origin()
def amazon():
    amazon_url = "https://www.amazon.in/s?k=iphone12"
    r = requests.get(amazon_url)

    # time.sleep(10)
    amazon_html = bs(r.content,"html5lib")
    # print(amazon_html.prettify())
    # content = amazon_html.findAll("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
    # content = amazon_html.findAll("span",{"class":"a-offscreen"})
    content = amazon_html.findAll("div",{"class":"sg-col-inner"})
    # print(content)
    del content[0]

    lis = []

    for d in content:
        try :
            name = d.div.h2.a.span.text
            rating = d.div.next_sibling.div.span['aria-label']
            price = d.div.next_sibling.next_sibling.div.div.div.div.a.span.span.text
            dic = {"name":name,"rating":rating,"price":price}
            lis.append(dic)
        
        except Exception as e:
            print("Something went wrong")
            print(e)
    
    return jsonify(lis)


# if __name__ == '__main__':
#     app.run(debug=True)
