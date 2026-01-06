import pandas as pd
from sqlalchemy import create_engine
import os

DATABASE_URL = "postgresql://admin:admin@postgres_db:5432/warehouse"

CLEAN_PATH = "/opt/airflow/data/clean_carts.csv"

# validasi file hasil transform ada
if not os.path.exists(CLEAN_PATH):
    raise FileNotFoundError(f"{CLEAN_PATH} not found")

engine = create_engine(DATABASE_URL)

df = pd.read_csv(CLEAN_PATH)

df.to_sql(
    "fact_carts",
    engine,
    if_exists="replace",
    index=False
)

print("Load to Postgres success")
