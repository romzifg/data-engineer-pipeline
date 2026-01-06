# End-to-End ETL Pipeline with Apache Airflow

## 📌 Project Overview
This project implements an end-to-end **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** to process e-commerce cart data.

The pipeline is developed and executed in a **Linux environment using WSL (Windows Subsystem for Linux)**, with a **Python virtual environment (`.venv`)** for dependency isolation during local development and testing.  
The system is fully containerized using Docker for orchestration and database services.

---

## 🧠 Problem Statement
Raw transactional data from external APIs is often not analytics-ready.
It may contain missing values, inconsistent data types, and lacks derived metrics.

This project addresses those challenges by building a reliable ETL pipeline that:
- Ingests data from a REST API
- Cleans and transforms raw data
- Loads structured data into a PostgreSQL data warehouse
- Is orchestrated and monitored using Apache Airflow

---

## 🎯 Objective
- Build an Airflow-based ETL pipeline
- Run the project in a Linux environment via WSL
- Use a Python virtual environment for dependency isolation
- Separate infrastructure concerns using Docker
- Automate extract, transform, and load processes
- Produce analytics-ready data

---

## 🏗 Architecture Diagram

![ETL Flow](diagrams/etl_flow.png)

---

## 🔄 ETL Pipeline Flow

### 1️⃣ Extract
- Located in `docker/airflow/etl/extract.py`
- Fetches cart data from a public REST API (`dummyjson.com`)
- Stores raw data as CSV in the data layer

### 2️⃣ Transform
- Located in `docker/airflow/etl/transform.py`
- Removes null values
- Ensures correct data types
- Adds derived metric `discount_rate`
- Outputs a clean CSV file

### 3️⃣ Load
- Located in `docker/airflow/etl/load.py`
- Loads transformed data into PostgreSQL
- Creates fact table `fact_carts`

---

## 🛠 Tech Stack

| Layer | Technology |
|------|-----------|
Orchestration | Apache Airflow |
Data Processing | Python (Pandas) |
Data Source | REST API |
Data Warehouse | PostgreSQL |
Infrastructure | Docker & Docker Compose |
Environment | WSL (Linux) + Python Virtual Environment |
OS | Windows (via WSL) |

---

## ▶️ Local Development Environment (WSL)

This project is developed and tested using **WSL (Windows Subsystem for Linux)** to ensure a Linux-compatible environment similar to production systems.

A Python virtual environment is used for dependency isolation when running scripts locally:

```bash
python -m venv .venv
source .venv/bin/activate
```

## How To Run (Docker)
### Start PostgreSQL
```bash
cd docker/db
docker-compose up -d
```

### Start Airflow
```bash
cd docker/airflow
docker-compose up -d
```

### Access Airflow UI
```bash
http://localhost:8080

Username: airflow
Password: airflow
```

## Output
- Cleaned and transformed cart data
- PostgreSQL fact table: fact_carts
- Fully automated ETL workflow managed by Airflow DAGs