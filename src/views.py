
from flask import (
    Blueprint,
    request,
    url_for,
    redirect,
    render_template,
)


bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    quick_links = {
        'save_emails': url_for('views.save_emails'),
    }
    return render_template('home.jinja2', quick_links=quick_links)


@bp.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    msg = ''

    if request.method == 'POST':
        try:
            event_id = int(request.form['event_id'])
            email_subject = str(request.form['email_subject'])
            email_content = str(request.form['email_content'])
            timestamp = request.form['timestamp']
        except (KeyError, ValueError):
            msg = "BadRequest"

        # return redirect(url_for('views.save_emails'))

        print("Form:", request.form)

    return render_template('save_email.jinja2', msg=msg)
