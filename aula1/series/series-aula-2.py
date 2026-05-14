import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Criando o conjunto de dados fake (40 itens)
np.random.seed(42) # Para resultados reproduzíveis
s1 = pd.Series(np.linspace(10, 100, 40), name="Base")
s2 = pd.Series(np.random.uniform(1, 5, 40), name="Ajuste")

# 2. Utilizando as operações aritméticas
s_soma = s1 + s2
s_sub  = s1 - s2
s_mult = s1 * s2
s_div  = s1 / s2
s_exp  = s2 ** 2  # Elevando o ajuste ao quadrado para não estourar a escala

# 3. Organizando em um DataFrame para facilitar o plot
df_results = pd.DataFrame({
    'Soma (+)': s_soma,
    'Subtração (-)': s_sub,
    'Multiplicação (*)': s_mult,
    'Divisão (/)': s_div,
    'Exponenciação (**)': s_exp
})

# 4. Gerando o gráfico
plt.figure(figsize=(12, 6))
df_results.plot(ax=plt.gca(), marker='o', markersize=4)

plt.title('Operações Aritméticas com Pandas Series', fontsize=14)
plt.xlabel('Índice do Item (0-39)')
plt.ylabel('Valor Resultante')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title="Operações")
plt.tight_layout()
plt.show()