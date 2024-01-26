import os
from dotenv import load_dotenv
import pandas as pd
from calculateDF import calculateStatusAndFinalGrade


def find_numberOfClasses(URL: str) -> int:
    return int(pd.read_csv(
        f"{URL.replace('/edit?usp=sharing', '/export?format=csv')}").iloc[0].iloc[0][28:])


def main():
    load_dotenv()
    URL = str(os.getenv("URL"))
    numberOfClasses = find_numberOfClasses(URL)
    df = pd.read_csv(
        f"{URL.replace('/edit?usp=sharing', '/export?format=csv')}", skiprows=2)
    print(df)
    print(calculateStatusAndFinalGrade(df, numberOfClasses))


if __name__ == "__main__":
    main()
