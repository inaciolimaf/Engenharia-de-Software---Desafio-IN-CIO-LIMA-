import pandas as pd
from student import Student


def calculateStatusAndFinalGrade(df: pd.DataFrame, numberOfClasses) -> pd.DataFrame:
    df['Situação'] = df['Situação'].astype(str)
    for i, row in df.iterrows():
        student = Student(row["Faltas"], row["P1"],
                          row["P2"], row["P3"], numberOfClasses)
        situation = student.situation()
        df.at[i, "Situação"] = situation
        df.at[i, "Nota para Aprovação Final"] = student.final_grade(
        ) if situation == "Exame Final" else 0
    return df
