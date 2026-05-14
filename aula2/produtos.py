import pandas as pd

df = pd.read_csv('./aula2/estoque_produtos_100_itens.csv', 
                sep=";"
            )

print()
print("df.head(3)")
print(df.head(3))
print()
print("df.tail(3)")
print(df.tail(3))
print()
print("df[\"Codigo\"]") # Busca de uma coluna, operações ele usa tudo, traz o head e o tail da coluna no print
print(df["Codigo"]) # Busca de uma coluna, traz o head e o tail da coluna no print
print()
print("df[['Codigo', 'Preco']]") 
print(df[['Codigo', 'Preco']]) 

# iloc -> seleciona por posição
linha1 = df.iloc[0] # Objeto que contem todos os campos de uma linha do dataframe
linha1a3 = df.iloc[0:3]  # Cria um subDataframe que contem apenas as linhas selecionadas

print()
print("linha1") 
print(linha1) 

print()
print("linha1a3") 
print(linha1a3) 

# loc -> seleciona por nome
print("df.loc[2]") 
print(df.loc[2]) # Indice igual ao iloc

subDataFrame = df.loc[1:5, ['Vencimento','Descricao']]
print("subDataFrame") 
print("subDataFrame") 
print("subDataFrame") 
print(subDataFrame)