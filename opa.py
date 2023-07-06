import pandas as pd



df_notas = pd.read_csv(r"data\notas.csv")

df_etudantes = pd.read_csv("data\estudantes.csv")

df_disciplinas = pd.read_csv("data\disciplinas.csv")

# resultado = pd.merge(pd.merge(df_notas, df_etudantes, on='id_estudante', how='inner'), df_disciplinas, on='id_disciplina', how='inner')


resultado = pd.merge(df_notas, df_etudantes, on="id_estudante", how="inner")

print(resultado.head())