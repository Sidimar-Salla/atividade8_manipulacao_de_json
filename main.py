import dash
import dash_bootstrap_components as dbc
from dash import Dash, html, dcc

app = Dash(external_stylesheets=[
                        dbc.themes.BOOTSTRAP,
                        dbc.icons.FONT_AWESOME
                        ], 
           use_pages=True,
          )

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("EducaControl", className="display-6"),
        html.Hr(),
        html.P(
            "Escolha uma opção a baixo", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Dashboard", href="/", active="exact"),
                dbc.NavLink("Relatórios", href="/relatorios", active="exact"),
                dbc.NavLink("Opções", href="/opcoes", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(dash.page_container, id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

if __name__ == "__main__":
    app.run_server(debug=True)