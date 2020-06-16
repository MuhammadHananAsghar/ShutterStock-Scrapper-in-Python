'''CREATED BY MUHAMMAD HANAN ASGHAR
DATA SCIENTIST
PYTHONIST
'''
import requests
from bs4 import BeautifulSoup as Soup
import string
def SpiderShutter(search):
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent" : USER_AGENT}
    soup = Soup(requests.get(f"https://www.shutterstock.com/search/{search}",headers=headers).content,"html.parser")
    a = soup.find_all('div',class_="z_b_c")[0].text
    num = []
    total = ""
    for i in a:
        if i in string.digits:
            num.append(i)
    total = "".join(num)
    if int(total) > 5:
        total = 5
    else:
        pass
    links = []
    for i in range(total):
        soup = Soup(requests.get(f"https://www.shutterstock.com/search/{search}?page={i}",headers=headers).content,"html.parser")
        a = soup.find_all('img')
        for i in a:
            if i.get('src') == None:
                pass
            else:
                links.append(i.get('src'))
    return links
a = SpiderShutter('bollywood')
