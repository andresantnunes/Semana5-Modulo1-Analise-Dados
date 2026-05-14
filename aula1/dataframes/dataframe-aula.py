import pandas as pd


# Criando um dict
data = {
    'Nome': ['Ana', 'Bruno', 'Carlos'], 
        # Colunas podem ter tipos diferentes entre sim
        # Porém dentro da coluna é só um tipo
    'Idade': [23, 35, 45], 
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
    }

# Transforma dict em dataframe
df = pd.DataFrame(data)
# print(df)

dados = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Cadeira'],
    'Preço': [80, 120, 900, 450],
    'Estoque': [45, 30, 12, 8]
}
df = pd.DataFrame(dados)
# print(df)

print("df.head(2)")
print(df.head(2))
print("df.tail(2)")
print(df.tail(2))
print("df.info()")
df.info()
print("df.describe()")
print(df.describe())
print("df.columns")
print(df.columns)