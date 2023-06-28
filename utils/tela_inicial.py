

def homePage():
    tamanho_coluna = 30 
    coluna1 = "Código"
    print(len(coluna1))
    print(
        coluna1 + ' '*(tamanho_coluna-(len(coluna1))) + '///'
    )

homePage()