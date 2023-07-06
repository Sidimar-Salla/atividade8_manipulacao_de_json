from utils.json_utils import JsonUtils
from utils.pandas_utils import PandasUtils

class UpdateDB:
    '''
        Classe usada para atualizar a base de dados
    '''
    def __init__(self) -> None:
        self.api_estudantes = "https://fmsampaio.github.io/helper-sites/json-examples/alunos.json"
        self.api_disciplinas = "https://fmsampaio.github.io/helper-sites/json-examples/disciplinas.json"

    def updateTableEstudantes(self):
        '''
            Função para atualizar a tabela Estudantes
        '''
        path_db = r"data\estudantes.csv"

        # Pegando os dados da API
        data = JsonUtils(
            url_api=self.api_estudantes
        ).__json__()

        # Laço de repetição
        for json in data:

            # Pega as infos para abastecer a tabela dos estudantes
            infos = {
                "id_estudante": json["id"],
                "nome": json["nome"]
            }

            # Verifica se o estudante já existe 
            if not PandasUtils().isExists(
                path=path_db,
                column1="id_estudante",
                value1=infos["id_estudante"],
                colunm2="nome",
                value2=infos["nome"]
            ):

                # Se o aluno não estiver na base de dados ele é adicionado
                PandasUtils().addInfo(
                    path=path_db,
                    infos=infos
                )

    def updateTableNotas(self):
        '''
            Função para atualizar a tabela Notas
        '''
        path_db = r'data\notas.csv'

        # Pegando os dados da API
        data = JsonUtils(
            url_api=self.api_estudantes
        ).__json__()

        # Laço de repetição 
        for json in data:

            # Adiciona o ID do estudante nos infos
            infos = {
                "id_estudante": json["id"]
            }

            # Pega a Pega a lista de disciplinas que o Estudante está
            list_disciplinas = json["disciplinas"]

            # Laço de Repetição
            for disciplina in list_disciplinas:

                # Pega o resto das informações
                infos["id_disciplina"] = disciplina["id"]
                infos["nota"] = disciplina["nota"]
                
                # Testa se o dado já existe
                if not PandasUtils().isExists(
                    path=path_db,
                    column1="id_estudante",
                    value1=infos["id_estudante"],
                    colunm2="id_disciplina",
                    value2=infos["id_disciplina"]
                ):
                    
                    # Adiciona a informação
                    PandasUtils().addInfo(
                        path=path_db,
                        infos=infos
                    )

                # else:

                #     # Salva o valor por cima

        

    def updateTableDisciplinas(self):
        '''
            Função para atualizar a tabela Disciplinas
        '''
        path_db = r'data\disciplinas.csv'

        # Pegando os dados da API
        data = JsonUtils(
            url_api=self.api_disciplinas
        ).__json__()

        # Laço de Repetição
        for json in data:

            # Pega as informações dentro do Json
            infos = {
                "id_disciplina": json["id"],
                "nome": json["nome"],
                "credito": json["creditos"]
            }

            # Testa para ver se já existe a Disciplina
            if not PandasUtils().isExists(
                path=path_db,
                column1="id_disciplina",
                value1=infos["id_disciplina"],
                colunm2="nome",
                value2=infos["nome"]
            ):
                
                # Não existir adiciona na base
                PandasUtils().addInfo(
                    path=path_db,
                    infos=infos
                )
   