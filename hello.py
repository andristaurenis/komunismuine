from os.path import join
from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/<path:any_path>')
def serve_static_folder(any_path):
    return redirect(url_for('static', filename=any_path))

@app.route('/<lang>/<path:any_path>', methods = ['POST'])
def petition_form(lang, any_path):
    app.logger.warning([request.form['name'], request.form['email'], request.form['adult']])
    return 'no content', 204

@app.route('/')
def root():
    return redirect('/en/', code=301)

@app.route('/en/')
def en():
    return redirect('/en/index.html', code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
