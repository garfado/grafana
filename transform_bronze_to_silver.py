from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2
import json
def transform_to_silver():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="brewery_data",
        user="brewery_data",
        password="102030"
    )
    cur = conn.cursor()

    # Extrair dados da camada Bronze
    cur.execute("SELECT id, raw_data, ingest_time FROM bronze_beer_sales")
    rows = cur.fetchall()

    # Transformar e inserir na camada Silver
    for row in rows:
        raw_data = row[1]  # O raw_data já é um dict
        cur.execute("""
            INSERT INTO silver_beer_sales (customer_name, beer_name, quantity, order_date, ingest_time)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            raw_data["customer_name"], 
            raw_data["beer_name"], 
            raw_data["quantity"], 
            raw_data["order_date"], 
            row[2]
        ))

    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id="transform_bronze_to_silver",
    start_date=datetime(2024, 12, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    transform_task = PythonOperator(
        task_id="transform_to_silver",
        python_callable=transform_to_silver
    )

