
import os
import pandas as pd
import requests
from recommend import movieRecommend
from moviextra import movies_year
from movieinfo import movie_posters

file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

movie_data = pd.read_csv('movie_dataset.csv')

mr = movieRecommend()

posters = movie_posters('speed')


print(posters)
# def movie_complete(movie):
#     i =0 
#     movies = mr.movie_recommend(movie)
#     years = movies_year(movies)
#     for movie in movies:
#         base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie,years[i])
#         response = requests.get(base_url)
#         print(response.json())
#         print()
#         print("----------------------------------------")
#         print()
#         i +=1

# movie_complete('avatar')