from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2

def aggregate_to_gold():
    # Conexão com o banco de dados
    conn = psycopg2.connect(
        host="localhost",
        database="brewery_data",
        user="brewery_data",
        password="102030"
    )
    cur = conn.cursor()

    # Agregar dados da camada Silver para Gold
    cur.execute("""
        INSERT INTO gold_beer_sales (beer_name, total_quantity, total_sales, last_updated)
        SELECT 
            beer_name,
            SUM(quantity) AS total_quantity,
            COUNT(*) AS total_sales,
            NOW() AS last_updated
        FROM silver_beer_sales
        GROUP BY beer_name
        ON CONFLICT (beer_name) DO UPDATE 
        SET 
            total_quantity = EXCLUDED.total_quantity,
            total_sales = EXCLUDED.total_sales,
            last_updated = EXCLUDED.last_updated;
    """)

    conn.commit()
    cur.close()
    conn.close()

with DAG(
    dag_id="aggregate_silver_to_gold",
    start_date=datetime(2024, 12, 1),
    schedule_interval=None,
    catchup=False
) as dag:
    aggregate_task = PythonOperator(
        task_id="aggregate_to_gold",
        python_callable=aggregate_to_gold
    )

