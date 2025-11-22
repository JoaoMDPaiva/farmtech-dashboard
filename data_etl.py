# BLOCO DEMONSTRATIVO: Gerar dados anonimizados e pipeline para ML

import pandas as pd

# Este exemplo simula um pipeline de dados agrícolas gerados ou anonimizados.
# Não contém nenhuma conexão nem dado sensível.

# Exemplo de COMO SERIA a conexão:
"""
import oracledb
user = "usuario_exemplo"
password = "senha_exemplo"
...
cursor.execute("SELECT PH, NPK_N, NPK_P, NPK_K, LDR_MV, SOIL_PCT FROM IRRIGATION_DATASET")
...
"""

# ---- USAR APENAS O BLOCO FICTÍCIO/SIMULADO ABAIXO ----
df = pd.DataFrame({
    "PH": [6.1, 6.4, 7.0, 5.5],
    "NPK_N": [250, 270, 260, 240],
    "NPK_P": [180, 175, 190, 160],
    "NPK_K": [300, 320, 310, 295],
    "LDR_MV": [600, 615, 610, 590],
    "SOIL_PCT": [55.2, 48.9, 62.0, 47.1]
})

# EDA mínima
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Remove só linhas onde SOIL_PCT está ausente (target: umidade de solo)
df_clean = df.dropna(subset=['SOIL_PCT'])
print(df_clean.shape)

# Features e target
features = ['PH', 'NPK_N', 'NPK_P', 'NPK_K', 'LDR_MV']
X = df_clean[features]
y = df_clean['SOIL_PCT']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 80% treino / 20% teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Métricas
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nMétricas do modelo:")
print(f"MAE:  {mae:.2f}")
print(f"MSE:  {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.2f}")

# Salvar para dashboard - nome genérico para CSV seguro
df_clean.to_csv('dados_limpos.csv', index=False)
