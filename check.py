import requests
from recommend import movieRecommend
from moviextra import movies_year
import os
import pandas as pd
import random
import numpy as np
file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

df = pd.read_csv(file_path)

df = df.take(np.random.permutation(len(df))[:10])
random_movies = list(df['original_title'])
print(random_movies)

# def movies_data(movies,years):
#     posters = []
#     genres = []
#     ratings = []
#     datas = {}
#     i=0
#     for movie,year in zip(movies,years):
#         try:
#             base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=c5229271".format(movie,year)
#             response = requests.get(base_url)
#             print(response.status_code)
#             data = response.json()
#             poster = data.get('Poster')
#             posters.append(poster)
#             genre = data.get('Genre')
#             genres.append(genre)
#             rating = data.get('imdbRating')
#             ratings.append(rating)
#             print(poster)
#             print(genre)
#             print(rating)
#             print('*********************************')
#         except:
#             posters.append('N/A')
#             ratings.append('N/A')
#             genres.append('N/A')
#         datas['ratings'] = ratings
#         datas['posters'] = posters
#         datas['genres'] = genres
#     return datas