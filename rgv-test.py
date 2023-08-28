import pandas as pd
from bs4 import BeautifulSoup
import requests

def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                       "lxml") #converting the html to text

    #gets all the organizarion names
    orgs = []
    info = []
    #array of divs
    orgDiv = respTxt.find_all("div", class_ = "motopress-text-obj")
    for elem in orgDiv:
        orgs.append(elem.find("h3").text)
        info.append(elem.find("p"))


    #attempt at accessing the bolded into for future organizeing
    # for i in info:
    #     print(i.find_all("b"))
    #combine the lists into a dictionary
    orgInfoList = dict(zip(orgs, info))
    print(len(orgInfoList))
    print(len(orgs))
    print(len(info))
    for i in orgInfoList:
        print(i, orgInfoList[i])

url = "https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR05x4U45A48LqJ7XggcW5eIxy9b2DK9OkGmdBYck3sWjtQy_3U4sYMiMns"
getData(url)