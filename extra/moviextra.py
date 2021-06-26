import pandas as pd
import os
import numpy as np
import requests
from bs4 import BeautifulSoup


file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

movie_data = pd.read_csv(file_path)

def movies_year(movies):
    movies_year = []
    for movie in movies:
        try:
            year = movie_data[movie_data.title == movie]['release_date'].values[0]
            year = year.split("-")
            movies_year.append(year[0])
        except:
            movies_year.append('0000')
    return movies_year

def movie_year(movie):
    try:
        year = movie_data[movie_data.title == movie]['release_date'].values[0]
        year = year.split("-")
        year = year[0]
    except:
        year = "0000"
    return year


def random_movies():
    df = movie_data.take(np.random.permutation(len(movie_data))[:9])
    random_movies = list(df['original_title'])
    return random_movies

def getImages(soup) :
  data= {}
  image_urls = []
  imagelist = soup.find('div',{"class" : "media_index_thumb_list"})
  
  Image_anchors_list=[]
  if imagelist!= None :
      Image_anchors_list=imagelist.findAll('a')

  
  for a in Image_anchors_list :
    img = { }
    img["image_title"]=""
    if a.has_attr('title'):
        img["image_title"] = a['title']
    img['url']=""
    imageTagList = a.findAll('img')
    if len(imageTagList) > 0 :
      img['url'] = imageTagList[0]['src']
    image_urls.append(img)

  return image_urls


def ImageParse(ImdbId) :
    imdb_domain = "https://www.imdb.com" 
    url = "https://www.imdb.com/title/"+ImdbId+"/mediaindex"
    next_page=url
    while next_page!="" :
            print(next_page)
            r = requests.get(url=next_page)
            soup = BeautifulSoup(r.text, 'html.parser')
            try: 
                  a= soup.findAll('a',{'class': 'prevnext'})[1]
                  next_page =imdb_domain + a['href']
                  if "Next" not in a.string :
                      next_page=""
            except Exception as e:
                print(e,"next-page did not found")
                next_page=""
            try :    
                img=getImages(soup)
            except Exception as e: 
                print(e,"soup-exception")
                break
    return img