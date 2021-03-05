import requests
from recommend import movieRecommend
from moviextra import movies_year

mr =movieRecommend()
movies = mr.movie_recommend('avatar')
print(movies)
years = movies_year(movies)
print(years)


def movies_data(movies,years):
    posters = []
    genres = []
    ratings = []
    datas = {}
    i=0
    for movie,year in zip(movies,years):
        try:
            base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=c5229271".format(movie,year)
            response = requests.get(base_url)
            print(response.status_code)
            data = response.json()
            poster = data.get('Poster')
            posters.append(poster)
            genre = data.get('Genre')
            genres.append(genre)
            rating = data.get('imdbRating')
            ratings.append(rating)
            print(poster)
            print(genre)
            print(rating)
            print('*********************************')
        except:
            posters.append('N/A')
            ratings.append('N/A')
            genres.append('N/A')
        datas['ratings'] = ratings
        datas['posters'] = posters
        datas['genres'] = genres
        print(datas)
    return datas
    
# def movies_data(movies,years):
# 	posters = []
# 	i = 0
# 	for movie,year in zip(movies,years):
# 		try:
# 			base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=c5229271".format(movie,year)
# 			response = requests.get(base_url)
# 			print(response.status_code)
# 			data = response.json()
# 			print(data)
# 			data = data.get('Poster')
# 			posters.append(data)
# 			i = i+1
# 		except:
# 			posters.append('N/A')
# 	return posters

movies_data(movies,years)
