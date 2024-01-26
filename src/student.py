import math


class Student:
    def __init__(self, absences: int, p1: float, p2: float, p3: float, numberOfClasses: int) -> None:
        self.MAX_ALLOWED_ABSENCES_AS_A_PERCENTAGE = 25
        self.FINAL_APPROVAL_NOTE = 50
        self.absences = int(absences)
        self.p1 = int(p1)
        self.p2 = int(p2)
        self.p3 = int(p3)
        self.numberOfClasses = int(numberOfClasses)

    def situation(self):
        if self.absences > self.numberOfClasses*(self.MAX_ALLOWED_ABSENCES_AS_A_PERCENTAGE/100):
            return "Reprovado por Falta"
        mean = (self.p1+self.p2+self.p3)/3
        if mean < 50:
            return "Reprovado por Nota"
        if mean < 70:
            return "Exame Final"
        return "Aprovado"

    def final_grade(self):
        media = (self.p1+self.p2+self.p3)/3
        return int(math.ceil(self.FINAL_APPROVAL_NOTE*2 - media))
