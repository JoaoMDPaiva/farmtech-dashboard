import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

#Carregamento e limpeza dos dados
@st.cache_data
def load_data():
    df = pd.read_csv("dados_limpos.csv")
    df_clean = df.dropna(subset=["SOIL_PCT"])
    return df_clean

df = load_data()

#Título e Introdução do Dashboard
st.title("Assistente Agrícola Inteligente – Previsão da Umidade do Solo")
st.markdown("""
Este painel une sensores agrícolas reais, Machine Learning e visualização para prever a umidade do solo,
oferecer recomendações de irrigação/fertilização e apoiar decisões rápidas e inteligentes no campo.

*As decisões e recomendações seguem boas práticas de Agricultura de Precisão.*
""")

#Seleção das variáveis (features) e variável-alvo
features = ['PH', 'NPK_N', 'NPK_P', 'NPK_K', 'LDR_MV']  # Sensores/indicadores importantes
X = df[features]
y = df['SOIL_PCT']  # Variável alvo: umidade do solo

#Pipeline de Machine Learning
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#Avaliação do Modelo com Métricas de Regressão
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

col1, col2 = st.columns(2)
with col1:
    st.metric("MAE", f"{mae:.2f}", help="Erro absoluto médio: mostra o erro médio das previsões em relação ao real. Quanto menor, melhor.")
    st.metric("RMSE", f"{rmse:.2f}", help="Raiz do erro quadrático médio: destaca erros mais altos e é comum em agricultura.")
with col2:
    st.metric("MSE", f"{mse:.2f}", help="Erro quadrático médio: valor alto indica que as previsões estão distantes do real.")
    st.metric("R²", f"{r2:.2f}", help="Coeficiente de determinação: valores próximos de 1 indicam boa precisão do modelo.")

st.markdown("""
- **MAE (Erro Absoluto Médio):** Mostra o erro médio entre a previsão e o valor real.
- **RMSE (Raiz do Erro Quadrático Médio):** Penaliza erros altos, bastante usado em medições de campo.
- **MSE (Erro Quadrático Médio):** Parecido com RMSE, mas não tem ajuste de escala.
- **R² (Coeficiente de determinação):** Mede o quanto o modelo explica a variação dos dados; perto de 1 é excelente, negativo ou próximo de zero pede revisão do modelo/dados.
""")

#Sugestão automática de manejo agrícola baseada na previsão média
st.subheader("Sugestão Inteligente para Manejo")
umidade_media_prevista = y_pred.mean()
if umidade_media_prevista < 60:
    st.warning("→ Atenção: Umidade prevista baixa. Recomenda-se irrigação na próxima janela! (Boas práticas de Agricultura de Precisão)")
elif umidade_media_prevista > 90:
    st.info("→ Umidade prevista muito alta. Evite irrigação no momento. (Monitoramento contínuo recomendado)")
else:
    st.success("→ Umidade adequada prevista. Siga monitorando antes de irrigar.")

#Visualização aprimorada: Histograma real com Matplotlib
st.subheader("Distribuição da Umidade do Solo")
fig, ax = plt.subplots()
ax.hist(df['SOIL_PCT'], bins=15, color='skyblue', edgecolor='black')
ax.set_xlabel('Umidade do Solo (%)')
ax.set_ylabel('Nº de Registros')
ax.set_title('Histograma da Umidade do Solo')
st.pyplot(fig)

#Visualização: Tabela de correlações das features com a variável alvo
st.subheader("Correlação das Features com SOIL_PCT")
st.dataframe(df.corr(numeric_only=True)['SOIL_PCT'].sort_values(ascending=False))

#Simulador de Cenários com comentários didáticos
st.divider()
st.subheader("Simulador Interativo de Cenário Agrícola")
st.markdown("""
Digite valores dos sensores para simular um cenário e ver o que seria recomendado pelo sistema inteligente.  
Use dados típicos do seu campo para um teste realista!
""")
ph_sim = st.number_input("Informe o pH: (pH típico entre 5 e 8)", value=7.0)
npk_n_sim = st.number_input("NPK_N: (Nitrogênio, ex: 250)", value=250)
npk_p_sim = st.number_input("NPK_P: (Fósforo, ex: 180)", value=180)
npk_k_sim = st.number_input("NPK_K: (Potássio, ex: 300)", value=300)
ldr_mv_sim = st.number_input("LDR_MV: (Sensor de luminosidade, ex: 600)", value=600)

if st.button("Simular Previsão"):
    X_novo = np.array([[ph_sim, npk_n_sim, npk_p_sim, npk_k_sim, ldr_mv_sim]])
    umidade_predita = model.predict(X_novo)[0]
    st.write(f"Umidade prevista para o cenário informado: **{umidade_predita:.2f}%**")
    if umidade_predita < 60:
        st.warning("→ Recomenda-se irrigação nesse cenário! (Boas práticas de Agricultura de Precisão)")
    elif umidade_predita > 90:
        st.info("→ Evite irrigação: umidade já prevista muito alta.")
    else:
        st.success("→ Umidade adequada prevista. Siga monitorando.")

#Finalização didática do painel
st.divider()
st.markdown("""
> **Este painel reforça o conceito de Agricultura Cognitiva, onde IA e automação ajudam a transformar dados de campo em decisões ágeis, práticas e sustentáveis.  
Siga as recomendações e ajuste os sensores para maximizar o rendimento e a saúde da lavoura.**
""")

