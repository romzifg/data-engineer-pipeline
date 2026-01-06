import requests
import csv
import os

URL = "https://dummyjson.com/carts"

# DATA_DIR merupakan direktori shared volume antara Airflow dan container lain
# Folder ini digunakan agar hasil extract bisa dibaca oleh task transform
DATA_DIR = "/opt/airflow/data"

# raw_carts.csv merupakan nama file hasil extract data dari API
RAW_PATH = f"{DATA_DIR}/raw_carts.csv"

# memastikan folder data tersedia sebelum proses penulisan file
os.makedirs(DATA_DIR, exist_ok=True)

response = requests.get(URL)
response.raise_for_status()
data = response.json()["carts"]

# Proses menyimpan data ke file csv
# "w" merupakan mode write untuk menulis data ke dalam file
# newline="" digunakan untuk menghilangkan baris kosong tambahan pada csv
with open(RAW_PATH, "w", newline="") as f:
    writer = csv.writer(f)
    
    # Menambahkan header di file csv
    writer.writerow(["cart_id", "user_id", "total", "discounted_total"])

    # Proses looping data dari api lalu di inject ke dalam file csv
    for cart in data:
        writer.writerow([
            cart["id"],
            cart["userId"],
            cart["total"],
            cart["discountedTotal"]
        ])

print("Extract success")
