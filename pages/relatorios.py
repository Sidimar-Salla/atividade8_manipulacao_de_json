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
        self.df = PandasUtils().csvToDataframe(
            path="data\estudantes.csv"
        )

    @property
    def layout(self):
        self.load_data()
        return dbc.Container([
            dbc.Row([
                dbc.Col([
                    html.H1(
                        "Relatórios",
                        className="text-center"
                    ),
                    html.Hr(),
                ])
            ]),
            dbc.Row([

                # Primeiro Filtro
                dbc.Col([
                    html.H5('Base de Dados *'),
                    dcc.Dropdown(
                        ["Estudantes", "Disciplinas"],
                        id=self.id("value-database"),
                        multi=False
                    )
                ], width=4, 
                style={"background-color": "yellow"}, 
                className="p-4"),

                # Segundo Filtro
                dbc.Col([
                    html.Div(id=self.id("children-second-filter"))
                ], width=4, 
                style={"background-color": "yellow"}, 
                className="p-4"),  

                # Terceiro Filtro
                dbc.Col([
                    html.Div(id=self.id("children-third-filter"))
                ], width=4, 
                    style={"background-color": "yellow"},
                    className="p-4" 
                ),

            ])

        ])

    def events(self) -> None:
        @callback(
            Output(self.id("children-second-filter"), "children"),
            Input(self.id("value-database"), "value")
        )
        def updateSecondFilter(value):
            options = []
            if value is None:
                raise PreventUpdate()
            elif value == "Estudantes":
                list_options = PandasUtils().csvToDataframe(
                                    path="data\estudantes.csv"
                                )["nome"].sort_values().to_list()
            else:
                list_options = PandasUtils().csvToDataframe(
                                    path="data\disciplinas.csv"
                                )["nome"].sort_values().to_list()

            if value != []:
                return html.Div([
                    html.H5(value[:len(value)-1]),
                    dcc.Dropdown(
                        options=list_options,
                        id=self.id("value-second-filter"),
                        multi=False
                    )
                ])
        
        @callback(
            Output(self.id("children-third-filter"), "children"),
            Input(self.id("value-second-filter"), "value")
        )
        def updateThirdFilter(value):
            df = PandasUtils().csvToDataframe(
                                    path="data\estudantes.csv"
                                )
            
            df_notas = PandasUtils().csvToDataframe(
                                    path=r"data\notas.csv"
                                )
            
            df_disciplinas = PandasUtils().csvToDataframe(
                                    path="data\disciplinas.csv"
                                )
            
            get_id_estudante = df.loc[df["nome"] == value, "id_estudante"].values[0]

            cadeiras =df_notas.loc[df_notas["id_estudante"] == get_id_estudante, "id_disciplina"].values

            disciplinas = df_disciplinas.loc[df_disciplinas["id_disciplina"].isin(cadeiras), "nome"].values

            return html.Div([
                html.H5("Disciplina(s)"),
                dcc.Dropdown(
                    options=disciplinas,
                    id=self.id("value-second-filter"),
                    multi=True
                )
            ])




dash.register_page(__name__, path='/relatorios')

layout = RelatoriosPage().layout