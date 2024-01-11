import dash
import os
from wsgiref.simple_server import make_server

app = dash.Dash(__name__)

def hello_world():
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return str(message)

app.layout = dash.html.Div(hello_world())

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    server = make_server('0.0.0.0', port, app.server)
    server.serve_forever()
