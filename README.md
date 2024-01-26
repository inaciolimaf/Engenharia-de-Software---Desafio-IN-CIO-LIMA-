# Engenharia de Software - Desafio [INÁCIO LIMA]
## Desafio Tunts.Rocks 2024
This code aims to automatically fill in a Google spreadsheet about the student's situation based on grades and absences. The spreadsheet used to execute the code was [this]("https://docs.google.com/spreadsheets/d/1AOB0NWOnEr8DdKwWC0oxVl_AfsFl6-SbVXRthu6HxZI/edit?usp=sharing").
## How to run
- To run the code, the first step is creating a virtual environment

```python -m venv venv```

- Activate the environment

```.\venv\Scripts\activate```

- Install dependencies

```pip install -r requirements.txt```

- Put the URL of the file in Google Spreadsheets in the .env file

- If you do not have the credentials.json file, the code will show the result but will not change the file in the cloud

```python src/mainWithoutCredentials.py```

- If you have the credentials.json file, the code will also change the data file automatically. Place the file in the root of the project and run:

```python src/main.py```
##


