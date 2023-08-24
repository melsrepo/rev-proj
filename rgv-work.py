import pandas as pd
from bs4 import BeautifulSoup
import requests

#define a function
def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                            "lxml") #converting the html to text
    #gets all the organizarion names
    orgs = respTxt.find_all("h3", attrs={"aria-expanded": "true"})
    #gets the org info
    info = respTxt.find_all("p")
    #initialize keys
    res = dict(zip(orgs, info))

    arr = []
    # for elements in orgs:
    #     arr.append(elements.text)
    # for i in arr:
    #     print(i)

    # arr2 = []
    # for elements in info:
    #     arr2.append(elements.text)
    # for i in arr2:
    #     print(i)
    # return arr2
    for keys, value in res.items():
        print(keys)

def exportDate(data):
    df = pd.DataFrame(data)
    df.to_excel("rgv-sheet.xlsx")
getData("https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR1pt2PXiA7R94dHuUgvsWGURo7eLTKDySVz6t5dS_6xb1fFn1MH2jAnDkQ")
#exportDate(d)

