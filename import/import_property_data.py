from sqlalchemy import create_engine
import pandas as pd
import os

server = 'localhost'
database = 'Data'
username = 'SA'
password = 'YourStrongPassword123'
driver = 'ODBC Driver 17 for SQL Server'

# Tworzenie silnika SQLAlchemy
engine = create_engine(f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}')


path = "data/preprocessed_data/csv/"
files = os.listdir(path)[:50]

for _, file in enumerate(files):
    print(f"Import {_+1}/50")
    chunks = pd.read_csv(path+file, chunksize=1000)
    for chunk in chunks:
        df = chunk.iloc[:, 1:]
        df.to_sql("ARProperties", engine, if_exists='append', index=False)