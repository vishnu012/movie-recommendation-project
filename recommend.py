
import pandas as pd
import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import os


file_path = os.path.dirname(os.path.realpath(__file__)) + "/movie_dataset.csv"

movie_data = pd.read_csv(file_path)

class movieRecommend:
    
    def combine_features(self,row):
        try:
            return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']+" "+row['tagline']
        except:
            print("Error",row)

    
    def title_from_index(self,index):
        return movie_data[movie_data.index == index]['title'].values[0]


    def index_from_title(self,title):
        title_list = movie_data['title'].tolist()
        common = difflib.get_close_matches(title,title_list,1)
        title_sim = common[0]
        return movie_data[movie_data.title == title_sim]['index'].values[0]

    
    def movie_recommend(self,user_liked_movie):
        features = ['keywords','cast','genres','director','tagline']
        for feature in features:
            movie_data[feature] = movie_data[feature].fillna('')
        movie_data['combined_features'] = movie_data.apply(self.combine_features,axis=1)
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(movie_data['combined_features'])
        cosine_sim = cosine_similarity(count_matrix)
        movie_index = self.index_from_title(user_liked_movie)
        similer_movies = list(enumerate(cosine_sim[movie_index]))
        similer_movies_sorted = sorted(similer_movies,key=lambda x:x[1],reverse=True)
        i = 0
        movies_sorted = []
        for element in similer_movies_sorted:
            movies_sorted.append(self.title_from_index(element[0]))
            i = i+1
            if i>23:
                break
        return movies_sorted
