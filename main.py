import dash
import dash_bootstrap_components as dbc
from dash import Dash, html
from components.login import LoginComponent

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    LoginComponent().layout,
)

if __name__ == "__main__":
    app.run_server(debug=True)