import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from utils.pandas_utils import PandasUtils

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

    @property
    def layout(self):
        self.load_data()
        return dbc.Col([
            dbc.Row([

                # Card Quantidade de Alunos
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

                # Card Quantidade de Alunos
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



                
            ])
        ])

    def events(self) -> None:
        pass

dash.register_page(__name__, path='/')

layout = DashboardPage().layout
