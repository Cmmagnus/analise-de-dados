# Análise de Vendas em Marketplaces

Este projeto tem como objetivo realizar a análise de dados de vendas em diferentes marketplaces (AliExpress, Etsy, Shopee), utilizando Python para processamento de dados e visualização, além de explorar o poder do ChatGPT para realizar análises exploratórias por meio de prompts criados para entender melhor o comportamento das vendas, descontos e desempenho de produtos.

## Estrutura do Projeto

O projeto é dividido em duas partes principais:

### 1. **Análise com Prompts Criados para ChatGPT**

Utilizando o ChatGPT, criamos uma série de 10 prompts que foram alimentados com os dados de vendas para obter insights rápidos e explorar diferentes aspectos do comportamento de compra nos marketplaces. Esses prompts ajudam a entender as vendas, os produtos mais vendidos, o impacto dos descontos e outros fatores importantes.

Os **10 prompts** criados para análise de dados foram os seguintes:

1. Quais são os 5 produtos mais vendidos em cada marketplace (AliExpress, Etsy e Shopee)?
2. Qual foi o total de vendas (em valor) por marketplace nos últimos 3 meses?
3. Qual é o ticket médio das compras para cada marketplace?
4. Existe alguma correlação entre o uso de cupons de desconto e o aumento na quantidade de produtos vendidos?
5. Qual é o percentual de pedidos que receberam desconto em cada marketplace?
6. Quais são os 5 países que mais compram os produtos da Meganium?
7. Qual é a distribuição de idade dos compradores por marketplace?
8. Existe um período do mês ou do ano em que as vendas aumentam significativamente?
9. Qual é a média de produtos comprados por pedido em cada plataforma?
10. Quais são os produtos que possuem a maior variação de preço entre os marketplaces?

Esses prompts são enviados para o ChatGPT, e ele retorna respostas detalhadas com insights valiosos para a análise.

### 2. **Análise com Scripts Python**

Além da análise com o ChatGPT, o projeto também inclui scripts em Python para realizar uma análise detalhada e quantitativa dos dados de vendas. O código em Python processa os dados das vendas e realiza as seguintes análises:

1. **Análise de Vendas por Marketplace**: Calcula o total de vendas e a média de preços por plataforma.
2. **Produtos Mais Vendidos**: Identifica os 5 produtos mais vendidos em cada marketplace.
3. **Impacto dos Cupons de Desconto**: Analisa o impacto dos cupons de desconto nas vendas.
4. **Distribuição Geográfica das Vendas**: Mapeia os países com mais compras e suas respectivas quantidades.
5. **Ticket Médio e Quantidade por Pedido**: Calcula o ticket médio e a quantidade média de produtos comprados por pedido.

## Pré-requisitos

Para rodar o projeto, você precisará das seguintes dependências:

- Python 3.x
- Pandas
- Matplotlib

Você pode instalar as dependências com o comando:

```bash
pip install pandas matplotlib

```

# 🚀 **COMO RODAR O PROJETO?** 🚀

Para rodar esse projeto de forma tranquila, siga os passos abaixo com atenção 👇:

---

### 🔄 **1. CLONE OU FAÇA O DOWNLOAD** 🖥️

Clone o repositório ou baixe o projeto para sua máquina.

Se preferir, pode usar o comando abaixo para **clonar** diretamente via Git:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Ou baixe o arquivo compactado diretamente [aqui](https://github.com/seu-usuario/seu-repositorio/archive/main.zip).

---

### 🗂️ **2. LOCALIZE OS ARQUIVOS CSV** 📊

Os arquivos CSV com os dados de vendas devem estar localizados no **mesmo diretório** do script, ou ajuste os caminhos de acordo com o seu ambiente.

---

### ⚡ **3. EXECUTE O SCRIPT PRINCIPAL** 👨‍💻

Abra seu terminal ou prompt de comando e execute o script principal em Python com o seguinte comando:

```bash
python nome_do_arquivo.py
```

Após isso, relaxe e acompanhe os resultados que aparecerão na tela!

---

### 🌟 **EXEMPLO DE SAÍDA** 🌟

Quando você rodar o script, verá algo assim:

```
🔸 AliExpress - Total de Vendas: $1245.67, Preço Médio: $32.50
🔸 Etsy - Total de Vendas: $789.43, Preço Médio: $28.75
🔸 Shopee - Total de Vendas: $1134.56, Preço Médio: $30.00
```

---

### 🎯 **CONTRIBUIÇÕES** 🤝

**Quer ajudar a melhorar o projeto?** Não seja tímido! Crie um **fork** e envie um **pull request** com as suas contribuições. Toda ajuda é super bem-vinda. 🥳

---

### 📝 **LICENÇA** 📜

Este projeto está licenciado sob a **MIT License**. Para mais detalhes, consulte o arquivo LICENSE.

---

#### ✨ **Divirta-se programando!** ✨
