from flask import Blueprint, render_template, request, redirect, url_for
from .controller import add_to_waitlist, get_waitlist

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

@home.route("/waitlist", methods=['GET'])
def waitlist():
    """List users on waitlist."""
    return get_waitlist()