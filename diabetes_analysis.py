import pandas as pd

# Cargar el conjunto de datos
data = pd.read_csv('../data/diabetes.csv')

# Mostrar las primeras filas
print("Primeras filas del conjunto de datos:")
print(data.head())

# Descripción general
print("\nDescripción del conjunto de datos:")
print(data.describe())
