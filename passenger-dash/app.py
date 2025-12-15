import os
from dash import Dash, html

app = Dash(__name__, requests_pathname_prefix="/pun/dev/passenger-dash/")

app.layout = [html.Div(children="Hello World")]

if __name__ == "__main__":
    app.run(debug=True)
