import pandas as pd
import os
import requests
from sqlalchemy import create_engine

def download_data():
    data = []
    chunk_size = 5000 #maximum size allowed by api
    offset = 0
    base_url = 'https://data.cms.gov/data-api/v1/dataset/2f1e57ea-ac2f-4f62-aeb1-f8254307c395/data?'
    while True:
        response = requests.get(base_url + f'offset={offset}&size={chunk_size}')
        if response.status_code != 200:
            raise Exception(f"Error {response.status_code}: {response.text}")
        chunk = response.json()
        if not chunk:
            break
        data = data + chunk
        offset = offset + chunk_size

    df = pd.DataFrame(data)
    os.makedirs("data", exist_ok=True)
    df.to_csv('data/raw_data.csv', index=False)
    print("Downloaded CMS data.")
'''
def clean_data():
    df = pd.read_csv("data/raw_data.csv")
    df_cleaned = df.dropna()
    df_cleaned.to_csv("data/cleaned_data.csv", index=False)
    print("Cleaned and saved CMS data.")
'''
def load_to_db():
    DATABASE_URL = os.getenv("AIRFLOW__DATABASE__SQL_ALCHEMY_CONN")
    engine = create_engine(DATABASE_URL)
    df = pd.read_csv("data/raw_data.csv")
    df.to_sql("cms_data", con=engine, if_exists="replace", index=False)
    print("Loaded data into database.")