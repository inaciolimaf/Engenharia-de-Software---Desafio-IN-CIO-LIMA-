import os
from dotenv import load_dotenv
import pandas as pd
from calculoDataFrame import calculoSituacaoENotaFinal

load_dotenv()

# Acessar uma variável de ambiente
URL = str(os.getenv("URL"))

total_de_aulas = int(pd.read_csv(f"{URL.replace('/edit?usp=sharing', '/export?format=csv')}").iloc[0].iloc[0][28:])
# TODO: Passar para outra função
df = pd.read_csv(f"{URL.replace('/edit?usp=sharing', '/export?format=csv')}", skiprows=2)
print(df)
print(calculoSituacaoENotaFinal(df, total_de_aulas))