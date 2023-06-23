from flask import Blueprint, render_template, request, redirect, url_for
from .controller import add_to_waitlist

home = Blueprint("home", __name__)

@home.route("/")
@home.route("/home")
@home.route("/index")
def home_page():
    """Render the home page."""
    return render_template('home/index.html')


@home.route("/join_waitlist", methods=['GET', 'POST'])
def join_waitlist():
    """Join the waitlist."""
    return add_to_waitlist(request)