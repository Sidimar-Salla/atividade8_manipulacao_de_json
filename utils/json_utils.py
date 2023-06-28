import requests
import json

class JsonUtils:
    '''
        Classe usada para puxar as informações da API
    '''
    url_api:str

    def __init__(self, url_api) -> None:
        self.url = url_api

    def __json__(self) -> json:
        '''
            Função usada para fazer a requisição
        '''
        response = requests.get(self.url)

        if response.status_code==200:

            return response.json()
        
        else:
            raise (f"Erro ao importar json. Código do erro: {response.status_code}")




url = "https://fmsampaio.github.io/helper-sites/json-examples/disciplinas.json"
print(JsonUtils(url).__json__())