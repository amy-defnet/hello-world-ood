import os
from dash import Dash, html

# Get environment variables
port = int(os.environ.get("port"))
host = os.environ.get("host")

# Define base path (used when served behind a proxy)
base_url = f"/node/{host}/{port}/"

app = Dash(__name__, url_base_pathname=base_url)

# Requires Dash 2.17.0 or later
app.layout = [html.Div(children="Hello World")]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
