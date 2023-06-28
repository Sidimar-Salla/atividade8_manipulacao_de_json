import pandas as pd
import json

# Exemplo de JSON no formato de registros
json_data = [
    {"nome": "João", "idade": 30},
    {"nome": "Maria", "idade": 25},
    {"nome": "Pedro", "idade": 35}
]



# Ler o JSON com orient='records'
df = pd.DataFrame(json_data)

# Imprimir o DataFrame
print(df)
