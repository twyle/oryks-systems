from .forms import RegistrationForm
from flask import request, redirect, url_for, render_template, Request, flash
from http import HTTPStatus
from .models import User
from ...extensions.extensions import db_session
from sqlalchemy.exc import IntegrityError


def add_to_waitlist(request_object: Request) -> tuple[str, int]:
    """Add a user to the witalist."""
    form = RegistrationForm(request_object.form)
    error = ''
    if request_object.method == 'POST':
        if form.validate:
            email_address: str = form.email.data
            try:
                add_user(email_address)
            except IntegrityError:
                form.email.data = ''
                error = f'The user with the email address {email_address} already signed up!'
                flash(error)
            else:
                flash('Thanks for registering')
                return redirect(url_for('home.home_page'))
    return render_template('home/waitlist.html', form=form, error=error), HTTPStatus.OK

def add_user(email_address: str) -> None:
    """Add a uer to the wiatlist database."""
    user = User(email=email_address)
    db_session.add(user)
    db_session.commit()
    
def get_waitlist() -> list[User]:
    """Get users on the waitlist."""
    users = User.query.all()
    return users