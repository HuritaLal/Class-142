from flask import Flask,jsonify,request
import csv

all_movies=[]

with open("data.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

liked_movies=[]
not_liked_movies=[]
did_not_watch=[]

app=Flask(__name__)
@app.route('/get_movie')
def get_movie():
    return jsonify({
        "data":all_movies[0],
        'status':'success'
    })
    
@app.route('/liked_movies',methods=['POST'])
def liked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        'status':'success'
    }),201
    
@app.route('/unliked_movies',methods=['POST'])
def unliked_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    not_liked_movies.append(movie)
    return jsonify({
        'status':'success'
    }),201
    
@app.route('/not_watched_movies',methods=['POST'])
def not_watched_movies():
    movie=all_movies[0]
    all_movies=all_movies[1:]
    did_not_watch.append(movie)
    return jsonify({
        'status':'success'
    }),201
    
if __name__=="__main__":
    app.run()