import requests
from moviextra import movies_year


def movie_posters(movies,years):
	posters = []
	i = 0
	for movie,year in zip(movies,years):
		try:
			base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=c5229271".format(movie,year)
			response = requests.get(base_url)
			print(response.status_code)
			data = response.json()
			print(data)
			data = data.get('Poster')
			posters.append(data)
			i = i+1
		except:
			posters.append('N/A')
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