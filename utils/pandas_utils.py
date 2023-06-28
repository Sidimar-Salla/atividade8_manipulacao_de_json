import pandas as pd


class PandasUtils:
    '''
        Classe criada para usarmos funções que usam a biblioteca Pandas
    '''
    def __init__(self) -> None:
        self.path_notas = r"data\notas.csv"
        self.path_disciplinas = r"data\disciplinas.csv"
        self.path_estudantes = r"data\estudantes.csv"

    def csvToDataframe(self, path):
        '''
            Função usada para pegar o Dataframe da base de dados
        '''
        return pd.read_csv(path)

    def jsonToDataframe(self, json_data) -> dict:
        '''
            Transforma o json em um Dataframe
        '''
        return pd.DataFrame(json_data)
    
    def isExists(self, path, column, value) -> bool:
        '''
            Função para verificar se o valor existe do Dataframe
        '''

        # Pega o Dataframe
        df = self.csvToDataframe(path)

        # Retorna se existe os não
        return df[column].isin([value]).any()
    
    def addInfo(self, path, infos):
        '''
            Função usada para adicionar informação no Dataframe
        '''

        # Pega o Data frame
        df = self.csvToDataframe(path)

        # Adiciona a nova linha no final do DataFrame
        df.loc[len(df)] = infos

        # Salva o novo Dataframe
        df.to_csv(path, index=False)

        # Mensagem de sucesso
        print('Linha adicinada com sucesso!')



    

    