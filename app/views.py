from flask import render_template

from app import app
from .requests import get_movies

@app.route('/')
def movie():
    '''
    View movie page function that returns the movie details page and its data
    '''
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('home.html', title = title,popular = popular_movies)