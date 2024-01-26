import os
from dotenv import load_dotenv
import pandas as pd
import re
import numpy as np
from calculoDataFrame import calculoSituacaoENotaFinal
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


def extract_id(url: str) -> str:
    return str(re.search(r"/d/([^/]+)/", url).group(1))


load_dotenv()

# To access an environment variable
URL = str(os.getenv("URL"))

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = extract_id(URL)
SAMPLE_RANGE_NAME_WITH_TOTAL_OF_CLASSES = "engenharia_de_software!A2:H27"
SAMPLE_RANGE_NAME_WITHOUT_TOTAL_OF_CLASSES = "engenharia_de_software!A3:H27"

creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
        token.write(creds.to_json())


service = build("sheets", "v4", credentials=creds)
# Call the Sheets API
sheet = service.spreadsheets()
data = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                          range=SAMPLE_RANGE_NAME_WITH_TOTAL_OF_CLASSES).execute()["values"]
totalDeAulas = int(data[0][0][28:])
data.pop(0)
max_cols = max(len(row) for row in data)
# Preencher as linhas com menos colunas com NaN
for row in data:
    while len(row) < max_cols:
        row.append(np.nan)
df = pd.DataFrame(data[1:], columns=data[0])
df = calculoSituacaoENotaFinal(df, 60)
newData = [df.columns.tolist()]+df.values.tolist()
sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME_WITHOUT_TOTAL_OF_CLASSES,
                      valueInputOption="USER_ENTERED", body={'values': newData}).execute()
