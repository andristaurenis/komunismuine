from flask import Flask, redirect, url_for, flash
app = Flask(__name__)

@app.route('/')
def hello_world():
    #  return redirect(url_for('lt'))
    # return redirect('/lt/') # everything is so staic right now
    return "hello world"

#  @app.route('/lt/')
#  def lt():
    #  return url_for('static', filename='index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
