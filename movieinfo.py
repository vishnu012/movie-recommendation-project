import requests

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
            
        except:
            posters.append('N/A')
            ratings.append('N/A')
            genres.append('N/A')
        datas['ratings'] = ratings
        datas['posters'] = posters
        datas['genres'] = genres
    return datas

# def movie_complete(movies):
#     years = movies_year(movies)
#     movies_info = []
#     i =0 
#     for movie in movies:
#         base_url = "http://www.omdbapi.com/?t={}&y={}&apikey=5c2d953".format(movie,years[i])
#         response = requests.get(base_url)
#         movies_info.append(response.json())
        
#     return movies_info