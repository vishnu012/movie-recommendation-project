from flask import Flask,render_template,request,url_for,redirect
from recommend import movieRecommend
from movieinfo import movie_posters
from moviextra import movies_year
import time


app = Flask(__name__)
mr = movieRecommend()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
    if request.method == 'POST':
        movie_name = request.form['movie_search']
    try:
        similar_movies = mr.movie_recommend(movie_name)
        print(similar_movies)
        years = movies_year(similar_movies)
        print(years)
        # posters = movie_posters(similar_movies,years)
        # print(posters)    
        return render_template('results.html',movies = similar_movies)
    except:
        return render_template('index.html',error = 'Movie not found ...')
    


if __name__ == '__main__':
    app.run(debug=True)