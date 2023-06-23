from flask import Blueprint, render_template, request, redirect, url_for

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
    # return render_template('home/waitlist.html')
    error_message = 'The '
    if request.method == 'POST':
        print(request.form)
        return redirect(url_for('home.home_page'))
    return render_template('resetrequest.html')