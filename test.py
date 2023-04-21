from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import requests
from bs4 import BeautifulSoup as bs

# site_url = "https://www.pricedekho.com/mobiles/apple-iphone-11-128gb-price.html"
# r = requests.get(site_url)
# site_html = bs(r.content,"html5lib")
# # print(site_html)
# content = site_html("table",{"class":"allvariant contentHold"})
# # print((content))
# print(len(content))
# tbody = content[0].findAll('tbody')
# # print(len(tbody))
# # print(len(tr))
# tr = tbody[0].findAll('tr')
# # print(len(tr))

# lis = []
# for d in tr:
#     src = d.td.img['src']
#     price = d.td.next_sibling.text
#     link = d.td.next_sibling.next_sibling.a['href']

#     dic = {"src":src,"price":price,"link":link}
#     lis.append(dic)

# print(lis)


# site_url = 'https://www.cashify.in/apple-iphone-13-price-in-india'
# r = requests.get(site_url)
# site_html = bs(r.content,"html5lib")
# # print(site_html.prettify())
# content = site_html.findAll("div",{"class","mui-style-1o0goxb"})
# print(content)



# site_url = "https://www.google.co.in/search?q=iphone+13&sxsrf=APwXEdesT9ywuzeggZTOLWJYw33eSWJa5w%3A1681999559236&source=hp&ei=x0ZBZOTkC7uO2roPq-2TwA4&iflsig=AOEireoAAAAAZEFU1-a3XCuKIor3HwpgLhuPM2pWbFFX&ved=0ahUKEwik5PPR0Lj-AhU7h1YBHav2BOgQ4dUDCAk&uact=5&oq=iphone+13&gs_lcp=Cgdnd3Mtd2l6EAMyCwguELEDEIAEEOUEMgsILhCABBCxAxDlBDILCAAQgAQQsQMQyQMyCwgAEIAEEJIDEMsBMggIABCABBCSAzILCC4QgAQQsQMQ5QQyCwguEIAEELEDEOUEMgUIABCABDIICAAQgAQQsQMyBQgAEIAEOgcIIxDqAhAnOgQIIxAnOgoILhDHARDRAxAnOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6CwgAEIoFELEDEIMBOg4ILhCABBCxAxDlBBDUAjoOCC4Q1AIQsQMQgAQQ5QQ6CAguEIAEEOUEUDxYvSRg_yZoAnAAeAGAAdUDiAH3GpIBBzItNC4yLjSYAQCgAQGwAQo&sclient=gws-wiz"
# r = requests.get(site_url)
# site_html = bs(r.content,"html5lib")
# # print(site_html.prettify())
# content = site_html.findAll("div",{"class":"pla-unit-container"})
# print(content)

amazon_url = "https://www.amazon.in/s?k=iphone12"
r = requests.get(amazon_url)
amazon_html = bs(r.content,"html5lib")
# print(amazon_html.prettify())
# content = amazon_html.findAll("h2",{"class":"a-size-mini a-spacing-none a-color-base s-line-clamp-2"})
# content = amazon_html.findAll("span",{"class":"a-offscreen"})
content = amazon_html.findAll("div",{"class":"sg-col-inner"})
print(content)
print(len(content))

# del content[0]
# print(len(content))

lis = []

# for d in content:
#     try :
#         name = d.div.h2.a.span.text
#         rating = d.div.next_sibling.div.span['aria-label']
#         price = d.div.next_sibling.next_sibling.div.div.div.div.a.span.span.text
#         print(name,rating,price)
#         dic = {"name":name,"rating":rating,"price":price}
#         lis.append(dic)
    
#     except Exception as e:
#         print("Something went wrong")
#         print(e)


# flipkart_url = "https://www.flipkart.com/search?q=iphone12"
# r = requests.get(flipkart_url)
# flipkart_html = bs(r.content,"html5lib")
# # print(flipkart_html.prettify())
# content = flipkart_html.findAll("div",{"class":"_13oc-S"})
# lis = []
# for d in content:
#     try:
#      src = d.div.div.div.div.div.div.img['src']
#      name = d.div.div.div.next_sibling.div.div.string
#      rating = d.div.div.div.next_sibling.div.div.next_sibling.span.div.text
#      price = d.div.div.div.next_sibling.div.next_sibling.div.div.div.string
#     except:
#      pass 
    
#     dict = {"price":price,"rating":rating,"name":name,"src":src}
#     lis.append(dict)

# print(lis[0:3])

# *******FLIPKART********
# flipkart_url = "https://www.flipkart.com/search?q=iphone12"
# r = requests.get(flipkart_url)
# flipkart_html = bs(r.content,"html5lib")
# print(flipkart_html.prettify())
# content = flipkart_html.findAll("div",{"class":"_13oc-S"})
# print(len(content))

# ************AMAZON***********
# amazon_url = "https://www.amazon.in/s?k=iphone14"
# r = requests.get(amazon_url)
# amazon_html = bs(r.content,"html5lib")
# print(amazon_html.prettify())
# content = amazon_html.findAll("div",{"class":"sg-row"})
# print(content)

# ******************CROMA****************
# croma_url = "https://www.croma.com/search/?q=iphone12"
# r = requests.get(croma_url)
# croma_html = bs(r.content,"html5lib")
# # print(croma_html.prettify())
# content = croma_html.findAll("div",{"class":"content-wrap"})
# print(content)



# site_url = "https://www.pricebefore.com/redmi-note-8-space-black-64-gb-4-gb-ram-p423232.html"
# r = requests.get(site_url)
# site_html = bs(r.content,"html5lib")
# print(site_html.prettify())
# content = site_html.findAll("div",{"class":"cmo-mod cmo-product-price-history"})
# print(len(content))
# print(content)


# searchString = input("Enter here")
# flipkart_url = "https://www.flipkart.com/search?q=" + "samsung"
# uClient = uReq(flipkart_url)
# flipkartPage = uClient.read()
# uClient.close()
# flipkart_html = bs(flipkartPage, "html.parser")
# print(len(flipkart_html.findAll("div")))
# print(flipkart_html.prettify())
# content = flipkart_html.find_all("div")
# print(content)

# site_url = "https://www.gadgets360.com/search?searchtext=iphone12"
# r = requests.get(site_url)
# site_html = bs(r.content,"html5lib")
# print(site_html.prettify())
# content = site_html.findAll("div",{"class":"k_prc_wrp"})
# print(len(content))
# print(content)



# site_url = "https://www.smartprix.com/products/?q=iphone12"
# r = requests.get(site_url)
# uClient = uReq(site_url)
# sitePage = uClient.read()
# uClient.close()
# site_html = bs(r.content,"html5lib")
# print(site_html.prettify())
# content = site_html.findAll("div",{"class":"sm-products list size-m img-long"})
# print(len(content))
# print(content)

# 91Mobiles
# site_url = "https://www.91mobiles.com/search_page.php?q=" + "iphone12"
# uClient = uReq(site_url)
# sitePage = uClient.read()
# uClient.close()
# site_html = bs(sitePage,"html.parser")
# print(site_html.prettify())
# content = site_html.findAll("div",{"class":"content_finder_grid"})
# print(len(content))
# print(content[0].prettify())


# site_url = "https://www.compareraja.in/search?c=all&q=" + "iphone11"
# uClient = uReq(site_url)
# sitePage = uClient.read()
# uClient.close()
# site_html = bs(sitePage,"html.parser")
# print(site_html.prettify())
# title = (site_html.title.string)
# print(title)
# content = site_html.findAll("div",{"class":"prodcut-listing"})
# print(content[0].prettify())




# site_url = "https://pricee.com/?q=" + "samsung"
# uClient = uReq(site_url)
# sitePage = uClient.read()
# print(sitePage)
# uClient.close()
# site_html = bs(sitePage, "html.parser")
# print()
# con = (site_html.findAll('a'))
# con = site_html.findAll("div",{"class":"wtb-deal-list clearfix"})
# con =  site_html.findAll("div")
# print(con)
# print(len(con))
# n = site_html.find(id="wtb_deal_list")
# print(n)
# con = site_html.findAll("ul", {"id": "wheretobuy"})
# print(con)
# con = site_html.findAll("div")
# print(con)

# title = site_html.title
# print(title.string)

# print(site_html)