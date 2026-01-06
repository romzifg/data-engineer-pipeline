import pandas as pd
import os

RAW_PATH = "/opt/airflow/data/raw_carts.csv"
CLEAN_PATH = "/opt/airflow/data/clean_carts.csv"

# Validasi file ada (anti silent error)
if not os.path.exists(RAW_PATH):
    raise FileNotFoundError(f"{RAW_PATH} not found")

# membaca file csv
df = pd.read_csv(RAW_PATH)

# menghilangkan baris yang memiliki nilai null
df = df.dropna()

# pastikan kolom total bertipe numerik
df["total"] = pd.to_numeric(df["total"], errors="coerce")

# hitung rate diskon
df["discount_rate"] = 1 - (df["discounted_total"] / df["total"])

# simpan hasil transform
df.to_csv(CLEAN_PATH, index=False)

print("Transform success")
