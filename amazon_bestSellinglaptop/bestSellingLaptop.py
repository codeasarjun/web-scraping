import requests

from bs4 import BeautifulSoup
url="https://www.amazon.in/gp/bestsellers/computers/1375424031"

respose=requests.get(url)

page_content=respose.text

doc=BeautifulSoup(page_content,'html.parser')

# _cDEzb_p13n-sc-css-line-clamp-3_g3dy1
laptop_title_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})

#print(laptop_title)

def get_laptop_title(doc):
    laptop_title_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})
    laptop_titles=[]
    for tag in laptop_title_tag:
        try:
            title=tag.find('span')
            laptop_titles.append(title.text)
        except:
            laptop_titles.append("No laptop found")
    return laptop_titles

print(get_laptop_title(doc)[:10]) # this will give top 10 laptop

import pandas as pd
# making csv file 
def get_Csv(doc):
    all_laptop={'Model Name': []}
    all_laptop["Model Name"]=get_laptop_title(doc)
    return all_laptop

csv_file=pd.DataFrame.from_dict(get_Csv(doc), orient='index')
csv_file=csv_file.transpose()
csv_file.to_csv('Top Selling Laptop.csv',index=None)





