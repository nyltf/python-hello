import dash
import os
from wsgiref.simple_server import make_server

app = dash.Dash(__name__)

app.layout = dash.html.Div('Hello world!')

if __name__ == '__main__':
#    app.run(debug=False)
    port = int(os.environ.get("PORT"))
    server = make_server('0.0.0.0', port, app.server)
    server.serve_forever()
