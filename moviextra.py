import pandas as pd
import os

file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

movie_data = pd.read_csv(file_path)

def movies_year(movies):
    movies_year = []
    for movie in movies:
        year = movie_data[movie_data.title == movie]['release_date'].values[0]
        year = year.split("-")
        movies_year.append(year[0])
    return movies_year