import time
import  requests
from bs4 import BeautifulSoup

url="here we need to provide best seller link from amazon .in  "
response= requests.get(url)
#print(response.status_code)
page_content=response.text
doc=BeautifulSoup(page_content, 'html.parser')
#print(page_content)

#print(len(page_content))

#print(page_content[:1000])




#extracting title of the book
book_title_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})

def get_book_title(doc):
    book_title_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})
    Book_Titles=[]
    for tag in book_title_tags:
        try:
            title_tag = tag.find('span')
            Book_Titles.append(title_tag.text)
        except :
            Book_Titles.append("Not Available")
    return Book_Titles
# this function will give the titles of the books

books=get_book_title(doc)[:10]       # titles of top ten  selling books on amazon

#print(a)

author_name_tags= doc.find_all('div',{'class':'zg-grid-general-faceout'})

def get_all_authors(doc):
    author_name_tags= doc.find_all('div',{'class':'zg-grid-general-faceout'})
    Author_Names=[]
    for tag in author_name_tags:
        try:
            Author_Names.append(tag.find('div',{'class':'a-row a-size-small'}).text)
        except :
            Author_Names.append("Not Available")
    return Author_Names
# This function will help to get the name of the authors
autors=get_all_authors(doc)[:10] 


#print(autors)

rating= 'a-icon a-icon-star-small a-star-small-4-5 aok-align-top'
rating_tags= doc.find_all('i',{'class': rating})

def get_all_stars(doc):
    rating_tags= doc.find_all('div',{'class':'zg-grid-general-faceout'})
    Stars=[]
    for tag in rating_tags:
        try:
            Stars.append(tag.find('span',{'class':'a-icon-alt'}).text)
        except :
            Stars.append("Not Available")
            
    return Stars

rating= get_all_stars(doc)[:10]



book_price_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})

def get_all_price(doc):
    book_price_tags= doc.find_all('div',{"class": "zg-grid-general-faceout"})
    Book_Price=[]
    for tag in book_price_tags:
        try:
            Book_Price.append(tag.find('span',{'class':'p13n-sc-price'}).text)
        except :
            Book_Price.append("Not Available")
            
    return Book_Price
price= get_all_price(doc)[:10]

#book URL


book_url_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})

book_url_tag0=book_url_tag[0].find('a',{'class':'a-link-normal'})

def get_all_url(doc):
    book_url_tag=doc.find_all('div',{"class": "zg-grid-general-faceout"})
    Book_Title_Urls=[]
    base_url="we neeed to provide base url of amazon"
    for tag in book_url_tag:
        try:
            Book_Title_Urls.append(base_url + tag.find('a',{'class':'a-link-normal'})['href'])
        except :
            Book_Title_Urls.append("Not Available")
    return Book_Title_Urls

book_link=get_all_url(doc)[:10]





# creating data frame

import pandas as pd

# At last extract all the details from a page
import time
def get_all_details(doc):
    all_books={'Title': [], 'Author': [], 'Stars': [], 'Price': [], 'URL': []}
    #doc = doc
    all_books['Title'] += get_book_title(doc)
    time.sleep(1)
    all_books['Author'] += get_all_authors(doc)
    time.sleep(1)
    all_books['Stars'] += get_all_stars(doc)
    time.sleep(1)
    all_books['Price'] += get_all_price(doc)
    time.sleep(1)
    all_books['URL'] += get_all_url(doc)
    time.sleep(1)
    
    return all_books

dataframe = pd.DataFrame.from_dict(get_all_details(doc), orient= 'index')
dataframe= dataframe.transpose()

dataframe.to_csv('books.csv',index=None)

get_all_details(doc)


    
