from flask import Blueprint, render_template

home = Blueprint("home", __name__)

@home.route("/")
@home.route("/home")
@home.route("/index")
def home_page():
    """Render the home page."""
    return render_template('home/index.html')