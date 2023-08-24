from bs4 import BeautifulSoup
import requests

#define a function
def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                            "lxml") #converting the html to text
    orgs = respTxt.find_all("h3", attrs={"aria-expanded": "true"})
    arr = []
    # for elements in orgs:
    #     arr.append(elements.text)
    # for i in arr:
    #     print(i)
    info = respTxt.find_all("p")
    arr2 = []
    for elements in info:
        arr2.append(elements.text)
    for i in arr2:
        print(i)

getData("https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR1pt2PXiA7R94dHuUgvsWGURo7eLTKDySVz6t5dS_6xb1fFn1MH2jAnDkQ")



