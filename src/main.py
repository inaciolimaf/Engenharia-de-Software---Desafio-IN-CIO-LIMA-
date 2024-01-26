import pandas as pd
import requests

class Aluno:
    
    def __init__(self, faltas: int, p1: float, p2:float, p3: float, totalAulas:int) -> None:
        self.MAXIMO_DE_FALTA_PORCENTAGEM = 25
        self.NOTA_APROVACAO_FINAL = 50
        self.faltas = faltas
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.totalAulas = total_de_aulas
    
    def situacao(self):
        if self.faltas > self.totalAulas*(self.MAXIMO_DE_FALTA_PORCENTAGEM/100):
            return "Reprovado por Falta"
        media = (self.p1+self.p2+self.p3)/3
        
        if media < 50:
            return "Reprovado por Nota"
        if media < 70:
            return "Exame Final"
        return "Aprovado"
        
    def notaFinal(self):
        media = (self.p1+self.p2+self.p3)/3
        return self.NOTA_APROVACAO_FINAL*2 - media
        # Arredondar

url = "https://docs.google.com/spreadsheets/d/1AOB0NWOnEr8DdKwWC0oxVl_AfsFl6-SbVXRthu6HxZI/edit?usp=sharing"
total_de_aulas = int(pd.read_csv(f"{url.replace('/edit?usp=sharing', '/export?format=csv')}").iloc[0].iloc[0][28:])
# TODO: Passar para outra função
df = pd.read_csv(f"{url.replace('/edit?usp=sharing', '/export?format=csv')}", skiprows=2)

for i, row in df.iterrows():
    aluno = Aluno(row["Faltas"], row["P1"], row["P2"], row["P3"], total_de_aulas)
    situacao = aluno.situacao()
    df.at[i, "Situação"] = situacao
    df.at[i, "Nota para Aprovação Final"] = aluno.notaFinal() if situacao=="Exame Final" else 0
print(df)
