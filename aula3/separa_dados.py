import pandas as pd

# 1. Carregar o arquivo CSV (notando que o delimitador do seu arquivo é ';')
df_estoque = pd.read_csv('estoque_produtos_100_itens.csv', sep=';')

# 2. Definir os padrões de Regex para cada categoria
# O caractere '|' funciona como o operador OU (OR) no regex
padrao_limpeza = r'(sabonete|creme dental|detergente|amaciante|shampoo|desinfetante)'

# Para os alimentos, podemos listar as palavras-chave principais do seu estoque
padrao_alimentos = r'(leite|queijo|suco|sal|óleo|arroz|creme|^[creme dental]|presunto|molho|ovos|café|açúcar|cereal|farinha|achocolatado)'

# 3. Criar o DataFrame de Produtos de Limpeza
# case=False garante que vai pegar tanto "Sabonete" quanto "sabonete"
# o .copy copia o dataframe resultante da operação em um novo objeto
df_limpeza = df_estoque[df_estoque['Descricao'].str.contains(padrao_limpeza, case=False, na=False)].copy()
df_limpeza['Categoria'] = "Limpeza"

# 4. Criar o DataFrame de Alimentos
df_alimentos = df_estoque[df_estoque['Descricao'].str.contains(padrao_alimentos, case=False, na=False)].copy()
df_alimentos['Categoria'] = "Alimentos"

# print(df_limpeza)
# print(df_alimentos)

# concatenar as tabelas
estoque_categorizado = pd.concat([df_limpeza,df_alimentos], axis=0, ignore_index=True)

# print(estoque_categorizado.tail(20))
# print()
# print()
# print()

# ordenação de valores por um campo
df_resultado = estoque_categorizado.sort_values('Codigo')
# print(df_resultado)


df_resultado= estoque_categorizado.sort_values('Preco')
# print(df_resultado)

df_resultado= estoque_categorizado.sort_values('Preco')
# print(df_resultado)
