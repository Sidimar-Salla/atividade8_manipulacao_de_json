import dash
from dash import html, Input, Output, dcc, callback
import dash_bootstrap_components as dbc
import hashlib
import pathlib

class HomeComponent:
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
            html.H1("É os guri!")
        )

    def events(self) -> None:
        pass

dash.register_page(__name__, path='/home')

layout = HomeComponent().layout
