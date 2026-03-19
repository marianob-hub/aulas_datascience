import pandas as pd
import matplotlib.pyplot as plt

# 1. Criando os dados da nossa simulação (Dicionário de Python)
dados = {
    'Participante': ['Carlos', 'Ana', 'Bruno', 'Mari', 'Ricardo'],
    'Frequencia': [3, 5, 0, 2, 4], # P1: Quantas vezes por semana
    'Interesse': [5, 2, 4, 3, 1],  # P2: Escala de 1 a 5
    'Modalidade': ['Futebol', 'Corrida', 'E-sports', 'Academia', 'Vôlei'] # P3
}

# Transformando em um DataFrame (Tabela do Pandas)
df = pd.DataFrame(dados)

# 2. Configurando a área de desenho (2 gráficos lado a lado)
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# --- GRÁFICO 1: Barras para Frequência Semanal (Quantitativo) ---
ax[0].bar(df['Participante'], df['Frequencia'], color='skyblue')
ax[0].set_title('Frequência de Exercícios (Vezes/Semana)')
ax[0].set_ylabel('Dias')
ax[0].set_xlabel('Participantes')

# --- GRÁFICO 2: Pizza para Modalidades (Categorias) ---
# Contamos quantas vezes cada modalidade aparece
contagem_esportes = df['Modalidade'].value_counts()
ax[1].pie(contagem_esportes, labels=contagem_esportes.index, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightgreen', 'coral', 'lightpink', 'orchid'])
ax[1].set_title('Distribuição de Modalidades')

# Ajustando o layout para não amassar os gráficos
plt.tight_layout()

# Exibindo na tela
plt.show()