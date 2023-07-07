import xlsxwriter

class CreateXslx:
    studant_name = str
    registration = str
    df_values = dict


    def __init__(self, studant_name, registration, df_values) -> None:
        self.studant_name = studant_name
        self.registration = registration
        self.df_values = df_values

    def createArquive(self):
        '''
            Cria o arquivo
        '''
        name_arquive = self.studant_name.replace(' ', '_')

        self.workbook = xlsxwriter.Workbook(f'boletim_{name_arquive}.xlsx') 

    def createWorksheet(self):
        '''
            Cria uma nova pagina do arquivo
        '''

        self.worksheet = workbook = self.workbook.add_worksheet() 

    def header(self):
        '''
            Faz o cabeçalho
        '''
        self.worksheet.write('B2', f'Aluno: {self.studant_name}')
        self.worksheet.merge('B2:E2')

        self.worksheet.write('B3', f'Matrícula: {self.registration}')
        self.worksheet.merge('B3:E3')

        self.worksheet.merge('B4:E4')

        self.worksheet.write('B5', 'Código')
        self.worksheet.write('B5', 'Disciplina')
        self.worksheet.write('B5', 'Crédito')
        self.worksheet.write('B5', 'Nota')

        for index, row in self.df_values.iterrows():

            self.worksheet

    