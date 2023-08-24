from bs4 import BeautifulSoup
import requests

#define a function
def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                            "lxml") #converting the html to text
    orgs = respTxt.find_all("h3", class_= "motopress-text-obj")
    print(orgs)
getData("https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR1pt2PXiA7R94dHuUgvsWGURo7eLTKDySVz6t5dS_6xb1fFn1MH2jAnDkQ")



