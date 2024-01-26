import math


class Aluno:
    def __init__(self, faltas: int, p1: float, p2: float, p3: float, totalAulas: int) -> None:
        self.MAXIMO_DE_FALTA_PORCENTAGEM = 25
        self.NOTA_APROVACAO_FINAL = 50
        self.faltas = int(faltas)
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.totalAulas = int(totalAulas)

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
        return math.ceil(self.NOTA_APROVACAO_FINAL*2 - media)
