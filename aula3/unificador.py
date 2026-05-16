import pandas as pd

df_produtos = pd.read_csv('produtos.csv', sep=';')
df_categorias = pd.read_csv('categorias.csv', sep=';')

merge_produto = pd.merge(
    df_produtos,df_categorias, on='idCategoria',
    how="left", validate="many_to_one"
)

# para uma linha de produtos temos uma unica categoria
# para uma linha de categoria há multiplos produtos com a mesma categoria
nova_ordem = ['Codigo', 'Descricao', 'idCategoria','Nome_Categoria' ,'Preco', 'Estoque', 'Vencimento']

# Reordenando
merge_produto = merge_produto[nova_ordem]
print(merge_produto)

agrupamento_cat = df_produtos.groupby("idCategoria")['Preco'].count()

print(agrupamento_cat)

# Agrega valores valores em um indice
# categoria agrega valores de preco
tabela_pivotada = merge_produto.pivot_table(values="Preco", index='Nome_Categoria', aggfunc='mean')

print(tabela_pivotada)
