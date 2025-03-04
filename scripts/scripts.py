"""
# Plano para o Projeto

Este projeto tem como objetivo realizar uma análise detalhada de dados de vendas em diferentes marketplaces (AliExpress, Etsy, Shopee). O foco principal é compreender o desempenho de vendas, o impacto de cupons de desconto, a distribuição geográfica dos compradores, e calcular métricas como ticket médio e a quantidade média de produtos por pedido.

## Objetivo do Projeto

O objetivo principal deste trabalho é desenvolver scripts em Python para analisar dados de vendas e gerar informações úteis que podem ser usadas para otimizar a performance das vendas em marketplaces online. A análise abrange as seguintes áreas:

1. **Análise de Vendas por Marketplace**: Determinar o total de vendas e o preço médio de cada produto por plataforma.
2. **Produtos Mais Vendidos**: Identificar os produtos mais vendidos em cada marketplace e observar os padrões de venda.
3. **Impacto dos Cupons de Desconto**: Verificar o impacto dos cupons de desconto nas vendas e identificar o percentual de pedidos que utilizam desconto.
4. **Distribuição Geográfica das Vendas**: Mapear os países com maior número de compras e observar a distribuição geográfica.
5. **Ticket Médio e Quantidade por Pedido**: Calcular o ticket médio das compras e a quantidade média de produtos adquiridos por pedido.

Ao longo deste trabalho, serão usados **pandas** para manipulação dos dados e **matplotlib** para gerar gráficos que ajudam a visualizar as informações de maneira clara.

## Etapas do Projeto

As etapas do projeto incluem o desenvolvimento dos scripts de análise de dados, como descrito abaixo.

"""

import pandas as pd
import matplotlib.pyplot as plt

# Carregar os arquivos CSV para cada marketplace
files = {
    "AliExpress": "/mnt/data/Meganium_Sales_Data_-_AliExpress.csv",
    "Etsy": "/mnt/data/Meganium_Sales_Data_-_Etsy.csv",
    "Shopee": "/mnt/data/Meganium_Sales_Data_-_Shopee.csv"
}

# Função para carregar os dados de vendas de todos os marketplaces
def carregar_dados():
    """
    Carrega os dados de vendas dos marketplaces a partir dos arquivos CSV.
    Retorna um dicionário contendo DataFrames para cada marketplace.
    """
    try:
        dataframes = {name: pd.read_csv(path) for name, path in files.items()}
        print("Dados carregados com sucesso!\n")
        return dataframes
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")
        return {}

# 1. Análise de Vendas por Marketplace
def analisar_vendas(dataframes):
    """
    Calcula o total de vendas e o preço médio por marketplace.
    """
    print("Analisando Vendas por Marketplace...")
    for name, df in dataframes.items():
        total_vendas = df['total_price'].sum()
        media_precos = df['unit_price'].mean()
        print(f"{name} - Total de Vendas: ${total_vendas:.2f}, Preço Médio: ${media_precos:.2f}")
    print("\n")

# 2. Produtos Mais Vendidos
def produtos_mais_vendidos(dataframes):
    """
    Identifica os 5 produtos mais vendidos em cada marketplace.
    """
    print("Analisando os Produtos Mais Vendidos...\n")
    for name, df in dataframes.items():
        top_produtos = df.groupby('product_sold')['quantity'].sum().nlargest(5)
        print(f"Top 5 produtos mais vendidos em {name}:")
        print(top_produtos, "\n")

# 3. Impacto dos Cupons de Desconto
def analisar_descontos(dataframes):
    """
    Analisa quantos pedidos utilizaram cupons de desconto e o impacto no volume de vendas.
    """
    print("Analisando o Impacto dos Cupons de Desconto...\n")
    for name, df in dataframes.items():
        pedidos_com_desconto = df[df['discount_value'] > 0].shape[0]
        total_pedidos = df.shape[0]
        percentual_desconto = (pedidos_com_desconto / total_pedidos) * 100
        print(f"{name} - Pedidos com desconto: {percentual_desconto:.2f}%")
    print("\n")

# 4. Distribuição Geográfica das Vendas
def distribuicao_geografica(dataframes):
    """
    Mapeia os países com mais compras e suas respectivas quantidades.
    """
    print("Analisando a Distribuição Geográfica das Vendas...\n")
    for name, df in dataframes.items():
        paises_mais_vendas = df['delivery_country'].value_counts().head(5)
        print(f"Top 5 países com mais vendas em {name}:")
        print(paises_mais_vendas, "\n")

# 5. Ticket Médio e Quantidade por Pedido
def ticket_medio(dataframes):
    """
    Calcula o ticket médio e a quantidade média de produtos comprados por pedido.
    """
    print("Analisando o Ticket Médio e Quantidade por Pedido...\n")
    for name, df in dataframes.items():
        ticket_medio = df['total_price'].mean()
        media_produtos = df['quantity'].mean()
        print(f"{name} - Ticket médio: ${ticket_medio:.2f}, Média de produtos por pedido: {media_produtos:.2f}")
    print("\n")

# Função principal para executar todas as análises
def executar_analises():
    """
    Carrega os dados e executa todas as análises (vendas, produtos, descontos, geografia e ticket médio).
    """
    dataframes = carregar_dados()
    
    if not dataframes:
        return
    
    # Executando as funções de análise
    analisar_vendas(dataframes)
    produtos_mais_vendidos(dataframes)
    analisar_descontos(dataframes)
    distribuicao_geografica(dataframes)
    ticket_medio(dataframes)

    # Gerando gráficos para visualização (opcional)
    gerar_graficos(dataframes)

# Função para gerar gráficos (exemplo de visualização)
def gerar_graficos(dataframes):
    """
    Gera gráficos simples para visualização dos dados, como total de vendas por marketplace.
    """
    print("Gerando gráficos de vendas...\n")
    
    # Exemplo de gráfico: Total de vendas por marketplace
    vendas = {}
    for name, df in dataframes.items():
        vendas[name] = df['total_price'].sum()
    
    plt.figure(figsize=(8, 6))
    plt.bar(vendas.keys(), vendas.values(), color='skyblue')
    plt.title('Total de Vendas por Marketplace')
    plt.xlabel('Marketplace')
    plt.ylabel('Total de Vendas ($)')
    plt.show()

# Executando o script
if __name__ == "__main__":
    executar_analises()
