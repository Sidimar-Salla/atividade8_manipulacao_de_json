import dash
from dash import html, Input, Output, dcc, callback, register_page
import dash_bootstrap_components as dbc
import hashlib
import pathlib


class LoginComponent:
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
        return dbc.Container(
            dbc.Row(    
                dbc.Col(            
                    dbc.Card(
                        [
                            dbc.Container(
                                [
                                    html.H3(
                                        "Login",
                                        className="text-center mt-5"
                                    ),

                                    dbc.Input(
                                        placeholder="Usuário",
                                        type="email", 
                                        id="example-email", 
                                        className="mx-auto p-2 mt-4 rounded-pill box-shadow-sm"
                                    ),
                                    
                                    dbc.Input(
                                        placeholder="Senha",
                                        type="password",
                                        id="example-password",
                                        className="mx-auto p-2 mt-3 rounded-pill",
                                    ),
                                    dbc.Button(
                                        children="Login",
                                        color="primary",
                                        className="d-grid gap-2 col-7 mx-auto mt-3 rounded-pill",
                                        href="home",
                                        n_clicks=0,
                                        id=self.id("submit-login")
                                    )
                                    
                                ],
                                className="mb-3 p-3",
                            ),
                            html.Div(
                                [
                                    
                                ],
                                className="mb-3 p-3",
                            ),
                        ],
                        className="rounded-5"
                    ),                
                    # style={
                    #     "background-color": "red"
                    # },
                    width=6,
                    className="p-3 col-md-6 offset-md-3",
                ),
            ),
            class_name="max-height"
        )

    def events(self) -> None:
        pass


register_page(__name__, path='/')

layout = LoginComponent().layout

