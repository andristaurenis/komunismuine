from flask import Flask, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def hello_world():
    #  return redirect(url_for('lt'))
    return redirect('/lt/') # everything is so staic right now

#  @app.route('/lt/')
#  def lt():
    #  return url_for('static', filename='index.html')
