from os import getenv 
from os.path import join, dirname
from dotenv import load_dotenv
from flask import Flask, redirect, url_for, request
from email_messages import get_email_message
import smtplib
import logging
import datetime
from logging.handlers import RotatingFileHandler


# Load .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
EMAIL = getenv('EMAIL')
EMAIL_PASS = getenv('EMAIL_PASS')

app = Flask(__name__)
logHandler = RotatingFileHandler('/flasklogs/info.log', maxBytes=100000, backupCount=1)
app.logger.addHandler(logHandler)

@app.route('/<path:any_path>')
def serve_static_folder(any_path):
    return redirect(url_for('static', filename=any_path))

@app.route('/<lang>/', methods = ['POST'])
def petition_form(lang):
    app.logger.warning([datetime.datetime.now().isoformat(), request.form['name'],
        request.form['email'], request.form['adult']])

    mail_server = smtplib.SMTP('smtp.gmail.com', 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.login(EMAIL, EMAIL_PASS)
    mail_server.sendmail(EMAIL, request.form['email'], get_email_message(lang))
    mail_server.quit()
    return 'no content', 204

@app.route('/')
def root():
    return redirect('/en/', code=301)

@app.route('/en/')
def en():
    return redirect('/en/index.html', code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
