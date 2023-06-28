import pandas as pd
from json_utils import JsonUtils


class PandasUtils:
    '''
        Classe criada para usarmos funções que usam a biblioteca Pandas
    '''
    def __init__(self) -> None:
        pass

    def teste(self, json):
        return pd.read_json(json)
    