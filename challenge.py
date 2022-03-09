from flask import Flask,jsonify,request
import csv
all_articles = []
with open("articles.csv",encoding = "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_articles = []
not_liked_articles = []

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-article",methods = ["POST"])
def liked_article():
    #movie = all_movies[0]
    all_articles = all_articles[1:]
    liked_articles.append(movie)
    return jsonify({
        "status":"success"
    })

@app.route("/unliked-article",methods = ["POST"])
def unliked_article():
    #Smovie = all_movies[0]
    all_articles= all_articles[1:]
    not_liked_articles.append(movie)
    return jsonify({
        "status":"success"
    })

if __name__ == "__main__":
    app.run()
