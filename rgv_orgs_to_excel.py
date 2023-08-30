import pandas as pd
from bs4 import BeautifulSoup
import requests

def getData(url):
    response = requests.get(url)
    respTxt = BeautifulSoup(response.text,
                       "lxml") #converting the html to text

    #array of divs
    orgDiv = respTxt.find_all("div", class_ = "motopress-text-obj")

    orgDict = {}


    count = 0
    for elem in orgDiv:
        #get the current info line
        str = elem.find("div", class_ = "ui-accordion-content").get_text().strip()
        #getting rid of data with commas
        str = str.replace(",", "")
        str = str.replace("Sullivan City", "Sullivan city").replace("Rio Grande City", "Rio Grande city")
        #make it easier to parse
        str = str.replace('Email', ',Email').replace('Phone', ',Phone').replace('Address', ',Address').replace('City', ',City')
        #splits into what will be key value pairs
        if str[0] == ",":
            str = str.replace(str[0],"",1)
        output = str.split(',')
        infoDict = {}
        for info in output:
            #list of the key value pairs
            info = info.split(':')
            infoDict[info[0].strip()] = info[1].strip()
        orgDict[(elem.find("h3").get_text())] = infoDict
    print(orgDict)
    return orgDict
def write_ex(data):
    df = pd.DataFrame.from_dict(data)
    df_trans = df.T #transposing the rows to columns
    df_trans.to_excel("rgv-sheet.xlsx")

url = "https://rgvpartnership.com/rgv-non-profit-organizations/?fbclid=IwAR05x4U45A48LqJ7XggcW5eIxy9b2DK9OkGmdBYck3sWjtQy_3U4sYMiMns"
result = getData(url)
write_ex(result)