from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import psycopg2

def load_csv_to_postgres():
    # Caminho do CSV
    csv_path = '/home/daniel/sales_beer/csv/beer_sales.csv'

    # Conexão com PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="brewery_data",
        user="brewery_data",
        password="102030"
    )
    cur = conn.cursor()

    # Ler o CSV
    df = pd.read_csv(csv_path)

    # Inserir dados na tabela Bronze
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO bronze_beer_sales (raw_data) VALUES (%s)",
            (row.to_json(),)
        )

    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id="sales_beer_dag",
    start_date=datetime(2024, 12, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    load_csv_task = PythonOperator(
        task_id="load_csv_to_bronze",
        python_callable=load_csv_to_postgres
    )


