# momdadsistrtillie

# kunpyuoowdr

from lpsm import app, db

from flask import render_template, request, url_for
from werkzeug.utils import redirect

from lpsm.config import KEY

@app.route('/', methods=['get', 'post'])
def landing():
    if request.method == 'post':
        if request.form.get('secret_key') == KEY:
            return render_template('index.html')
    return redirect(url_for('/'))


