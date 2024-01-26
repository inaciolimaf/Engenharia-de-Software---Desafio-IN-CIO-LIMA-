import pandas as pd
from Aluno import Aluno

def calculoSituacaoENotaFinal(df:pd.DataFrame, total_de_aulas) -> pd.DataFrame:
    df['Situação'] = df['Situação'].astype(str)
    for i, row in df.iterrows():
        aluno = Aluno(row["Faltas"], row["P1"], row["P2"], row["P3"], total_de_aulas)
        situacao = aluno.situacao()
        df.at[i, "Situação"] = situacao
        df.at[i, "Nota para Aprovação Final"] = aluno.notaFinal() if situacao=="Exame Final" else 0
    return df
