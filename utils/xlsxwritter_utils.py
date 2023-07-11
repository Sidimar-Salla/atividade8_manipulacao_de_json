import xlsxwriter

class CreateXslxHistoricoEscolar:
    studant_name = str
    registration = str
    df_values = dict


    def __init__(self, studant_name, registration, df_values, total_cred, media_geral) -> None:
        self.studant_name = studant_name
        self.registration = registration
        self.df_values = df_values
        self.total_cred = total_cred
        self.media_geral = media_geral

        # Roda a automação
        self.createArquive()
        self.createWorksheet()
        self.header()
        self.saveXlsx()

    def returnPath(self):
        '''
            retorna o path name de onde salvou o arquivo
        '''
        return self.path

    def createArquive(self):
        '''
            Cria o arquivo
        '''
        name_arquive = self.studant_name.replace(' ', '_')

        self.path = f'temp\historico_escolar_{name_arquive.lower()}.xlsx'

        self.workbook = xlsxwriter.Workbook(self.path) 

    def createWorksheet(self):
        '''
            Cria uma nova pagina do arquivo
        '''

        self.worksheet = self.workbook.add_worksheet()

        self.border_format = self.workbook.add_format({
            'border': 1,  # Largura da borda em pontos
            'border_color': 'black'  # Cor da borda (pode ser um código RGB, por exemplo)
        })

        self.worksheet.set_column('B:B', 10)
        self.worksheet.set_column('C:C', 30)
        self.worksheet.set_column('D:D', 10)
        self.worksheet.set_column('E:E', 10)

    def header(self):
        '''
            Faz o cabeçalho
        '''
        self.worksheet.merge_range('B2:E2', f'Aluno: {self.studant_name}', self.border_format)

        self.worksheet.merge_range('B3:E3', f'Matrícula: {self.registration}', self.border_format)

        self.worksheet.merge_range('B4:E4', '', self.border_format)

        self.worksheet.write('B5', 'Código', self.border_format)
        self.worksheet.write('C5', 'Disciplina', self.border_format)
        self.worksheet.write('D5', 'Crédito', self.border_format)
        self.worksheet.write('E5', 'Nota', self.border_format)


        for index, row in self.df_values.iterrows():

            print(f"{index} - {row['id_disciplina']} - {row['nome_y']} - {row['credito']} - {row['nota']}")

            # Digita o Código da Disciplina
            self.worksheet.write(f'B{6 + index}', row['id_disciplina'], self.border_format)
            
            # Digita o nome da disciplina
            self.worksheet.write(f'C{6 + index}', row['nome_y'], self.border_format)

            # Digita a quantidade de créditos da disciplina
            self.worksheet.write(f'D{6 + index}', row['credito'], self.border_format)
            
            # Digita por fim a nota do aluno
            self.worksheet.write(f'E{6 + index}', row['nota'], self.border_format)

        self.worksheet.merge_range(f'B{7 + index}:E{7 + index}', '', self.border_format)

        self.worksheet.merge_range(f'B{8 + index}:E{8 + index}', f'Total de Créditos Cursados: {self.total_cred}', self.border_format)
        
        self.worksheet.merge_range(f'B{9 + index}:E{9 + index}', f'Média Geral: {self.media_geral}', self.border_format)

    def saveXlsx(self):
        '''
            Função para salvar o arquivo
        '''
        self.workbook.close()

class CreateXslxRelatorioDisciplina:

    def __init__(self, disciplina, id_disciplina, credito, df) -> None:
        self.name_disciplina = disciplina
        self.id_disciplina = id_disciplina
        self.total_creditos = credito
        self.df_value = df

        self.createArquive()
        self.createWorksheet()
        self.tableContent()
        self.saveXlsx()

    def returnPath(self):
        '''
            retorna o path name de onde salvou o arquivo
        '''
        return self.path

    def createArquive(self):
        '''
            Cria o arquivo
        '''
        name_arquive = self.name_disciplina

        self.path = f'temp\{name_arquive.lower()}_relatorio.xlsx'

        self.workbook = xlsxwriter.Workbook(self.path) 

    def createWorksheet(self):
        '''
            Cria uma nova pagina do arquivo
        '''

        self.worksheet = self.workbook.add_worksheet()

        self.border_format = self.workbook.add_format({
            'border': 1,  # Largura da borda em pontos
            'border_color': 'black'  # Cor da borda (pode ser um código RGB, por exemplo)
        })

        self.worksheet.set_column('B:B', 10)
        self.worksheet.set_column('C:C', 30)
        self.worksheet.set_column('D:D', 10)

    def tableContent(self):
        '''
            Cria a tabela em si
        '''
        self.worksheet.merge_range('B2:D2', f'Disciplina: {self.name_disciplina}', self.border_format)

        self.worksheet.merge_range('B3:D3', f'Matrícula: {self.id_disciplina}', self.border_format)

        self.worksheet.merge_range('B4:D4', f'Número de créditos: {self.total_creditos}', self.border_format)

        self.worksheet.merge_range('B5:D5', '', self.border_format)

        self.worksheet.write('B6', 'Matrícula', self.border_format)
        self.worksheet.write('C6', 'Nome Aluno', self.border_format)
        self.worksheet.write('D6', 'Nota', self.border_format)

        for index, row in self.df_value.iterrows():

            self.worksheet.write(f'B{7 + index}', row['id_estudante'], self.border_format)
            self.worksheet.write(f'C{7 + index}', row['nome_x'], self.border_format)
            self.worksheet.write(f'D{7 + index}', row['nota'], self.border_format)

    def saveXlsx(self):
        '''
            Função para salvar o arquivo
        '''
        self.workbook.close()