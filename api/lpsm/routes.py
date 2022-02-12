# momdadsistrtillie

# kunpyuoowdr

from flask_login.utils import login_required
from lpsm import app, db
from lpsm.models import *
from flask import render_template, request, url_for
from werkzeug.utils import redirect
from flask_login import current_user, login_user, logout_user
from lpsm.config import KEY

@app.route('/secret_key', methods=['GET', 'POST'])
def landing():
    if request.method == 'POST':
        if request.form.get('secret_key') == KEY:
            return render_template('feed.html')
    else:
        if current_user.is_authenticated :
            return render_template('feed.html')
        else:
            return render_template('landing.html')

@app.route('/feed')
@login_required
def feed():
    listings = []
    for listing in Listing.query.filter_by(active=True).order_by(Listing.date):
        listings.append(listing)
    return render_template('feed.html', listings=listings)
