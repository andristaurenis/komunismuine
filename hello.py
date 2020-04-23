from os.path import join
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

@app.route('/<path:any_path>')
def serve_static_folder(any_path):
    return redirect(url_for('static', filename=any_path))

@app.route('/')
def root():
    return redirect('/en/', code=301)

@app.route('/en/')
def en():
    return redirect('/en/index.html', code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
