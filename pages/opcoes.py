import dash
from dash import html, Input, Output, dcc, callback, register_page
import dash_bootstrap_components as dbc
import hashlib
import pathlib
from dash.exceptions import PreventUpdate
from time import sleep

from services.update_db_service import UpdateDB



class OpcoesPage:
    def __init__(self) -> None:
        self._id = hashlib.md5(
            str(pathlib.Path(__file__).absolute()).encode()).hexdigest()
        self.events()

    def id(self, name):
        return f"{name}-{self._id}"

    def load_data(self) -> None:
        pass

    @property
    def layout(self):
        self.load_data()
        return dbc.Col([
            dbc.Row([
                html.H1("Atualizar Base de Dados", className="text-center"),
                html.Hr(),
            ]),
            dbc.Row([
                dbc.Spinner([
                    dbc.Button("Atualizar",
                            id=self.id("button-update"),
                            n_clicks=0,
                            ),
                    html.Br(),
                    dbc.Alert(
                        "Base de dados atualizado com sucesso!!!",
                        id=self.id("alert"),
                        dismissable=True,
                        fade=False,
                        is_open=False,
                    ),
                ]),
            ])

        ])

    def events(self) -> None:
        @callback(
            Output(self.id("alert"), "is_open"),
            Input(self.id("button-update"), "n_clicks")
        )
        def updateDb(n):
            if not n:
                raise PreventUpdate

            # Atualiza base de dados
            UpdateDB().updateTableDisciplinas()
            sleep(1)
            UpdateDB().updateTableEstudantes()
            sleep(1)
            UpdateDB().updateTableNotas()

            return True



register_page(__name__, path='/opcoes')

layout = OpcoesPage().layout

