from flask import Flask, render_template, url_for, request, redirect  #routing of flask
from flask_sqlalchemy import SQLAlchemy            # db
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DBname.db'   # possibly to connect an others db
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False             # this function should be deleted soon
db = SQLAlchemy(app)                                            # create db

if __name__ == "__main__":
  app.run(debug=True) # only for work development by enject the project debug=False

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(52), nullable=False)
  intro = db.Column(db.String(256), nullable=False)
  text = db.Column(db.Text, nullable=False)
  date = db.Column(db.DateTime, default=datetime)

  def __repr__(self):
    return '<Article %r>' % self.id
    
@app.route('/')     
@app.route('/home')
def index():          # it can be a few acts to redirect the user
  return render_template("templates\index.html")

@app.route('/about')
def about():
  return redirect("templates\about.html")

@app.route('/posts')
def posts():
  articles = Article.query.order_by(Article.date.desc()).all() 
  return render_template("posts.html", articles=articles)

@app.route('/posts/<int: id>')
def post_detail(id):
  article = Article.query.get(id)
  return render_template("post_detail.html", article=article)

@app.route('/posts/<int: id>/del')
def post_delete(id):
  article = Article.query.get_or_404(id)
  try:
    db.session.delete(article)
    db.session.commit()
    return redirect('/posts')
  except:
    return "error message of delete post"

@app.route('/create_article', methods = ['POST', 'GET'])
def create_article():
  if request.method == "POST":
    title = request.form['title']
    intro = request.form['intro']
    text = request.form['text']

    article = Article(title=title, intro=intro, text=text)

    try:
      db.session.add(article)       # push new object to db
      db.session.commit(article)    # save the object
      return redirect('/posts')          # remove user from the page
    except:
      return "error message"

  else:
   return render_template("create_article.html")

@app.route('/posts/<int: id>/update', methods = ['POST', 'GET'])
def update_article():
  article = Article.query.get(id)
  if request.method == "POST":
    article.title = request.form['title']
    article.intro = request.form['intro']
    article.text = request.form['text']

    try:
      db.session.commit(article)    # save the object
      return redirect('/posts')     # remove user from the page
    except:
      return "error message by the update"

  else:  
   article = Article.query.get(id)
   return render_template("post_update.html", article=article)


