
from datetime import datetime

from flask import (
    Blueprint,
    request,
    url_for,
    redirect,
    render_template,
)

from src.models import (
    Event,
    Mail,
    EventMail,
)


bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    quick_links = {
        'view_emails': url_for('views.view_emails'),
        'save_emails': url_for('views.save_emails'),
    }
    return render_template('home.jinja2', quick_links=quick_links)


@bp.route('/save_emails', methods=['GET', 'POST'])
def save_emails():
    msg = ''

    events = Event.select()

    time_format = '%Y-%m-%d %H:%M'

    timestamp = datetime.now().strftime(time_format)
    email_subject = ''
    email_content = ''

    if request.method == 'POST':
        event_id = request.form['event_id']
        timestamp = request.form['timestamp']
        email_subject = request.form['email_subject']
        email_content = request.form['email_content']

        try:
            send_time = datetime.strptime(timestamp, time_format)

            mail = Mail.create(subject=email_subject, content=email_content)
            EventMail.create(event_id=event_id, mail=mail, send_time=send_time)

            msg = "Success"
        except Exception:
            msg = "Failed"

    response_data = {
        'msg': msg,
        'events': events,
        'timestamp': timestamp,
        'email_subject': email_subject,
        'email_content': email_content,
    }
    return render_template('save_email.jinja2', **response_data)


@bp.route('/view_emails')
def view_emails():
    msg = ''

    event_mails = (
        Mail
        .select(
            Event.name.alias('event_name'),
            Mail.subject,
            EventMail.send_time,
            EventMail.sent,
        )
        .join(EventMail)
        .join(Event)
    ).dicts()

    response_data = {
        'event_mails': event_mails,
    }
    return render_template('view_emails.jinja2', **response_data)
