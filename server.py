from flask import Flask, render_template
import os
from wsgiref.simple_server import make_server

app = Flask(__name__, template_folder = '', static_folder = '')
            
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    server = make_server('0.0.0.0', port, app.server)
    server.serve_forever()
