import dash
import dash_bootstrap_components as dbc
from dash import Dash, html

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

app.layout = html.Div(
    [
        dbc.Spinner(
            dash.page_container,
            fullscreen_style =True,
            delay_hide=1000
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)