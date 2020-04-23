from os.path import join
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)

static_files = ['index.css', 'README.md', '/static/index-en.html']
@app.route('/<path:any_path>')
def serve_static_folder(any_path):
    assumed_static_path = join('/static', any_path)
    #  app.logger.debug(request.base_url)
    app.logger.debug(any_path)
    if assumed_static_path in static_files:
        return "yay"
        #  return app.send_static_file(assumed_static_path)
    return {any_path: assumed_static_path}

@app.route('/')
def hello_world():
    #  return redirect(url_for('lt'))
    # return redirect('/lt/') # everything is so staic right now
    return "hello world"

#  @app.route('/lt/')
#  def lt():
    #  return url_for('static', filename='index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
