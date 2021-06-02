import requests


movie_name = 'Avatar'
year ="2009"
base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie_name,year)

response = requests.get(base_url)


data = response.json()
print(data)
print(data.get('Poster'))