'''
1)
create templates for both of our routes. we add directory with html files: about.html, home.html
(=the templates for our home and about routes).
import render template function which is used for the template that we want to render.
2)
add some posts (postsList) that we want to display in our template... some dummy data such that we can see
how this is actually passed into our templates.
3)
'''


# import Flask class
from flask import Flask, render_template

app = Flask(__name__)



postsList = [
    {
        'author' : 'Corey Schafer',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=postsList)
#    return "<h1>Hello World!</h1>"


#this about function is returning the information for that page and in this case it's just an h1 heading
#with the text of "About Page".
@app.route("/about")

def about():
    return render_template('about.html', title='About')
#    return "<h1>About Page</h1>"


if __name__ == '__main__':
    app.run(debug=True)