from flask import Flask,render_template,request,url_for,redirect
from recommend import movieRecommend
from movieinfo import movie_posters
from moviextra import movies_year
import time


app = Flask(__name__)
mr = movieRecommend()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

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
        posters = movie_posters(similar_movies,years)
        print(posters)    
        return render_template('results.html',datas = zip(similar_movies,posters))
    except:
        return render_template('index.html',error = 'Movie not found ...')
    
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)