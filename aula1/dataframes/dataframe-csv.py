import pandas as pd

df = pd.read_csv('vendas_modelo.csv')

# head retorna os primeiros 5 itens por padrão 
# e pode mudar o numero de itens por parametro
print(df.head(2))


