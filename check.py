
import os
import pandas as pd
import requests
from recommend import movieRecommend
from moviextra import movies_year
from movieinfo import movie_posters

file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

movie_data = pd.read_csv(file_path)

mr = movieRecommend()

movies = mr.movie_recommend('speed')
years = movies_year(movies)

for movie,year in zip(movies,years):
    base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie,year)
    response = requests.get(base_url)
    print(response.json())
    print()
    print("----------------------------------------")
    print()