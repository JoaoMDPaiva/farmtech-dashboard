# Farmtech-dashboard
Dashboard IA para previsão de umidade do solo

# 🌱 Assistente Agrícola Inteligente – Previsão da Umidade do Solo

Este projeto apresenta um **dashboard interativo** que utiliza Inteligência Artificial (IA) e dados agrícolas para prever a umidade do solo e sugerir ações automáticas de manejo, integrando conceitos modernos de **Agricultura de Precisão**.

> **Todos os dados do projeto são anonimizados e utilizados somente para fins didáticos/acadêmicos, nunca expondo informações sensíveis ou pessoais.**

---

## 📋 Funcionalidades

- **Previsão de umidade do solo** com base em sensores (pH, NPK_N, NPK_P, NPK_K, LDR_MV)
- **Sugestão automática de irrigação e manejo agrícola** baseada na previsão do modelo
- **Visualização de métricas** do modelo de IA: MAE, MSE, RMSE, R² (com explicações)
- **Gráficos e tabelas** interativas para análise dos dados e correlações
- **Simulador**: insira valores e veja o resultado/recomendação em tempo real

---

## 🚀 Como executar localmente

1. **Clone o repositório ou baixe os arquivos**
git clone https://github.com/SEU_USUARIO/farmtech-dashboard.git
cd farmtech-dashboard

text
2. **Instale as dependências**
pip install -r requirements.txt

text
3. **Execute o dashboard**
streamlit run app.py

text
4. O painel abrirá no navegador padrão. Pronto!

---

## 🗂️ Arquivos do projeto

| Arquivo             | Descrição                                                         |
|---------------------|-------------------------------------------------------------------|
| `app.py`            | Código do dashboard inteligente em Streamlit                      |
| `dados_limpos.csv`  | Base de dados PRONTA e ANONIMIZADA para análise                   |
| `requirements.txt`  | Bibliotecas necessárias para rodar o dashboard                    |
| `README.md`         | (Este arquivo) Guia de uso e informações do projeto               |

---

## 📊 Sobre as métricas

- **MAE (Erro Absoluto Médio):** erro médio entre o valor previsto e o observado
- **RMSE (Raiz do Erro Quadrático Médio):** dá mais peso a grandes erros (penaliza mais)
- **MSE (Erro Quadrático Médio):** base para o cálculo do RMSE
- **R² (Coeficiente de Determinação):** indica o quanto o modelo explica da variação dos dados
- 
---

## 🔒 Segurança

- Não há publicação nem uso de dados pessoais/sensíveis (ex.: ID, nome, localização exata).
- O arquivo `dados_limpos.csv` contém somente dados agrícolas genéricos e anonimizados.
