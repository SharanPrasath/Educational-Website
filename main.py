from flask import Flask, render_template, request
import requests

posts = requests.get("https://api.npoint.io/eef8385f90c6039a0235").json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def get_all_posts():
    return render_template('courses.html', all_posts=posts)

@app.route('/course/<int:index>')
def show_posts(index):
    requested_post = None
    for course_post in posts:
        if course_post['id'] == index:
            requested_post = course_post
    return render_template('info.html', post=requested_post)


if __name__ == "__main__":

     app.run(debug=True)
