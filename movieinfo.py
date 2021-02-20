import requests
from moviextra import movies_year


def movie_posters(movies):
    years = movies_year(movies)
    posters = []
    i = 0
    for movie in movies:
        base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie,years[i])
        response = requests.get(base_url)
        data = response.json()
        data = data.get('Poster')
        posters.append(data)
        i = i+1
    return posters




# def movie_complete(movies):
#     years = movies_year(movies)
#     movies_info = []
#     i =0 
#     for movie in movies:
#         base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie,years[i])
#         response = requests.get(base_url)
#         movies_info.append(response.json())
        
#     return movies_info