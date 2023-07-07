import dash
from dash import html, Input, Output, dcc, callback, State
import dash_bootstrap_components as dbc
from dash.exceptions import PreventUpdate
import hashlib
import pathlib
from utils.pandas_utils import PandasUtils
import plotly.express as px

class DashboardPage:
    def __init__(self) -> None:
        self._id = hashlib.md5(
            str(pathlib.Path(__file__).absolute()).encode()).hexdigest()
        self.events()

    def id(self, name):
        return f"{name}-{self._id}"

    def load_data(self) -> None:
        self.num_disciplinas = len(PandasUtils().csvToDataframe("data\disciplinas.csv")["id_disciplina"])
        self.num_alunos = len(PandasUtils().csvToDataframe("data\estudantes.csv")["id_estudante"])
        self.list_disciplinas = PandasUtils().csvToDataframe("data\disciplinas.csv")["nome"].sort_values().values
        self.list_estudantes = PandasUtils().csvToDataframe("data\estudantes.csv")["nome"].sort_values().values

    @property
    def layout(self):
        self.load_data()
        return dbc.Col([
            dbc.Row([

                # Card Quantidade de Estudantes
                dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend('Estudantes'),
                            html.H5(self.num_alunos, id=self.id(
                                "quant-automations"))
                        ], style={"padding-left": "20px", "padding-top": "10px"}),
                        dbc.Card([
                            html.Div(className="fa-solid fa-user-gear",
                                    style={
                                        "color": "white",
                                        "textAlign": "center",
                                        "fontSize": 30,
                                        "margin": "auto",
                                    }),
                        ], color="primary", style={"maxWidth": 75, "height": 100, "margin-left": "-10px"}),
                    ])
                ], width=6),

                # Card Quantidade de Disciplinas
                dbc.Col([
                    dbc.CardGroup([
                        dbc.Card([
                            html.Legend('Disciplinas'),
                            html.H5(self.num_disciplinas, id=self.id(
                                "quant-automations"))
                        ], style={"padding-left": "20px", "padding-top": "10px"}),
                        dbc.Card([
                            html.Div(className="fa-solid fa-user-gear",
                                    style={
                                        "color": "white",
                                        "textAlign": "center",
                                        "fontSize": 30,
                                        "margin": "auto",
                                    }),
                        ], color="primary", style={"maxWidth": 75, "height": 100, "margin-left": "-10px"}),
                    ])
                ], width=6),               
            ], style={"margin": "10px"}),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        html.Legend("Filtros", className="card-title"),
                        html.Label("Selecionar Estudantes *"),
                        dcc.Dropdown(
                            options=self.list_estudantes,
                            id=self.id("dropdown-estudantes"),
                            clearable=False,
                            style={"width": "100%"},
                            placeholder="Selecionar",
                            multi=True,
                        ),
                        html.Label("Selecionar Disciplina"),
                        dcc.Dropdown(
                            options=self.list_disciplinas,
                            id=self.id("dropdown-disciplinas"),
                            clearable=True,
                            style={"width": "100%"},
                            multi=True,
                            placeholder="Selecionar",
                        ),
                        html.Br(),
                        dbc.Row([
                            dbc.Col(
                                dbc.Button(
                                    'Filtrar',
                                    id=self.id('button-submit'),
                                    className="d-grid gap-2 mx-auto",
                                    color='primary',
                                    n_clicks=0,
                                ),
                                width=6
                            ),
                            dbc.Col(
                                dbc.Button(
                                    'Limpar',
                                    id=self.id('button-clear'),
                                    className="d-grid gap-2 mx-auto",
                                    color='secondary',
                                    n_clicks=0),
                                width=6
                            ),
                        ]),
                    ], style={"height": "100%", "padding": "20px"}),
                ], width=4),
                dbc.Col([
                        dbc.Card(
                            dcc.Graph(

                                id=self.id('graph1'),
                                style={'height': "100%", "padding": "10px"},
                                
                            )
                        )
                    ], width=8),
                ], style={"margin": "10px"}),
        ])

    def events(self) -> None:
        @callback(
            [
                Output(self.id("dropdown-estudantes"), 'value'),
                Output(self.id("dropdown-disciplinas"), 'value'),  
            ],
            Input(self.id('button-clear'), 'n_clicks'),
            prevent_initial_call=True
        )
        def cleanFilter(n_clicks):
            if n_clicks is None:
                raise PreventUpdate
            else:
                return None, None
            
        @callback(
            Output(self.id('graph1'), 'figure'),
            Input(self.id('button-submit'), 'n_clicks'),
            [
                State(self.id("dropdown-estudantes"), 'value'),
                State(self.id("dropdown-disciplinas"), 'value'),
            ],
            prevent_initial_call=True
        )
        def updateFigure(n_clicks, value_aluno, value_disciplina):
            if n_clicks is None:
                raise PreventUpdate()
            else:
                df = PandasUtils().mergeAllTables()

                df = df[["nome_x", "nome_y", "nota"]]

                if not value_aluno is None:

                    df = df.loc[df["nome_x"].isin(value_aluno)]

                if not value_disciplina is None:

                    df = df.loc[df["nome_y"].isin(value_disciplina)]

                if value_aluno is None:
                    fig = px.scatter(df,
                                x="nome_x",
                                y="nota",
                                title='Gráfico de Notas',
                                color='nome_y',
                                )

                else:
                    fig = px.scatter(df,
                                    x="nome_y",
                                    y="nota",
                                    title='Gráfico de Notas',
                                    color='nome_x',
                                    )
                    
                return fig
                




dash.register_page(__name__, path='/')

layout = DashboardPage().layout
