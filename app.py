from flask import Flask,render_template,request,url_for,redirect
from recommend import movieRecommend
from movieinfo import movies_data,movie_detail
from moviextra import movies_year,random_movies,movie_year
import time


app = Flask(__name__)
mr = movieRecommend()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def home():
    rmovies = random_movies()
    ryears = movies_year(rmovies)
    datas = movies_data(rmovies,ryears)
    posters = datas['posters']
    ratings = datas['ratings']
    genres = datas['genres']
    return render_template('index.html',datas = zip(posters,rmovies,genres,ratings))

@app.route('/results',methods=['POST'])
def results():
    if request.method == 'POST':
        movie_name = request.form['movie_search']
    try:
        similar_movies = mr.movie_recommend(movie_name)
        years = movies_year(similar_movies)
        datas = movies_data(similar_movies,years)
        posters = datas['posters']
        ratings = datas['ratings']
        genres = datas['genres']
        return render_template('results.html',datas = zip(posters,similar_movies,genres,ratings))
    except:
        return render_template('index.html',error = 'Movie not found ...')

@app.route('/details')
def details():
    moviename = request.args.get('movie_name',None)
    movieyear = movie_year(moviename)
    moviedetails = movie_detail(moviename,movieyear)
    print(moviedetails)
    return render_template('details.html',details=moviedetails)  


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)