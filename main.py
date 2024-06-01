from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)
posts = requests.get("https://api.npoint.io/4925f51e8be3ace259b9").json()

@app.route("/")
def home():
    url = requests.get("https://api.npoint.io/4925f51e8be3ace259b9")
    return render_template("index.html", blog=url.json())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
