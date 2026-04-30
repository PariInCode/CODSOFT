from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

books = pd.read_csv("books.csv")

books["features"] = books["author"] + " " + books["genre"]

cv = CountVectorizer()
matrix = cv.fit_transform(books["features"])
similarity = cosine_similarity(matrix)

def recommend(book_name):
    try:
        index = books[books["title"].str.lower() == book_name.lower()].index[0]
        scores = list(enumerate(similarity[index]))
        sorted_books = sorted(scores, key=lambda x: x[1], reverse=True)[1:6]

        recommended = []
        for i in sorted_books:
            row = books.iloc[i[0]]
            recommended.append({
                "title": row["title"],
                "image": row["image"],
                "link": row["link"]
            })

        return recommended
    except:
        return []

@app.route("/", methods=["GET", "POST"])
def home():
    recommendations = []

    if request.method == "POST":
        book = request.form["book"]
        recommendations = recommend(book)

    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)