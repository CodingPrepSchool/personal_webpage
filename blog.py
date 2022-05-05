from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


@app.route("/")
def index_page():
    blog = Blog(csrf_enabled=False)
    return render_template("index.html",template_form = blog)