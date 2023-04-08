import pandas as pd 
from flask import Flask, jsonify, request
import csv

df= pd.read_csv('movies.csv')

all_movies= []
with open('movies.csv') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]
    
liked_movies = []
disliked_movies = []
didnotwatch = []

app = Flask(__name__)

@app.route('/get-movie')
def get_movies():
    return jsonify({
        'data':all_movies[0],
        'status':'success',
    })
    
@app.route('/liked-movie',methods=['POST'])
def liked_movies():
    movie = all_movies[0]
    all_movies= all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':'success',
    })
    
@app.route('/disliked-movie',methods=['POST'])
def disliked_movies():
    movie = all_movies[0]
    all_movies= all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        'status':'success',
    })
    
@app.route('/did-not-watch',methods=['POST'])
def did_not_watch_movies():
    movie = all_movies[0]
    all_movies= all_movies[1:]
    didnotwatch.append(movie)
    return jsonify({
        'status':'success',
    })
    
if __name__ == '__main__':
    app.run()