import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from dash.exceptions import PreventUpdate
from utils.pandas_utils import PandasUtils

class RelatoriosPage:
    def __init__(self) -> None:
        self._id = hashlib.md5(
            str(pathlib.Path(__file__).absolute()).encode()).hexdigest()
        self.events()

    def id(self, name):
        return f"{name}-{self._id}"

    def load_data(self) -> None:
        self.list_estudantes = PandasUtils().csvToDataframe("data\estudantes.csv")["nome"].sort_values().values
        self.list_disciplinas = PandasUtils().csvToDataframe("data\disciplinas.csv")["nome"].sort_values().values

    @property
    def layout(self):
        self.load_data()
        return dbc.Container([
            dbc.Row([
                html.H1("Relatórios", className="text-center"),
                html.Hr(),

                dbc.Tabs([

                    dbc.Tab(
                        [
                            dbc.Row([
                                dbc.Card([
                                    dbc.CardBody([
                                        html.P("Selecione o estudante que desejas gerar o Histórico Escolar", className="card-text"),


                                        # html.Label("Selecionar Estudantes *"),
                                        dcc.Dropdown(
                                            options=self.list_estudantes,
                                            id=self.id("dropdown-estudantes"),
                                            clearable=False,
                                            style={"width": "100%"},
                                            placeholder="Selecionar",
                                            multi=False,
                                        ),

                                    ], className="mt-2"),
                                    dbc.CardFooter([
                                        dbc.Button("Gerar", color="success", id=self.id("submit-historico-escolar"))           
                                    ], className="mt-2"),

                                ], className="mt-2")
                            ])
                        ], 
                        label="Histórico Escolar", 
                        tabClassName="flex-grow-1 text-center"),
                    dbc.Tab(
                        dbc.Card([
                                    dbc.CardBody([
                                        html.P("Seleciona a disciplina que desejas gerar o relatório", className="card-text"),

                                        # html.Label("Selecionar Estudantes *"),
                                        dcc.Dropdown(
                                            options=self.list_disciplinas,
                                            id=self.id("dropdown-disciplina"),
                                            clearable=False,
                                            style={"width": "100%"},
                                            placeholder="Selecionar",
                                            multi=False,
                                        ),

                                    ], className="mt-2"),
                                    dbc.CardFooter([
                                        dbc.Button("Gerar", color="success", id=self.id("submit-relatorio-disciplina"))           
                                    ], className="mt-2"),

                                ], className="mt-2"),
                        label="Notas por Disciplina", 
                        tabClassName="flex-grow-1 text-center"),

                ])

            ])

        ])

    def events(self) -> None:
        pass
        
dash.register_page(__name__, path='/relatorios')

layout = RelatoriosPage().layout