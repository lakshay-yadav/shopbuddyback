import requests
from bs4 import BeautifulSoup
  
URL = "https://www.flipkart.com/search?q=" + "samsung"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())

table = soup.find('div', attrs = {"id":"container"})
st=str(table.div)
print(type(st))

if 'wtb_deal_list' in st:
    print(True)

