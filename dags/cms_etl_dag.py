#%%
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import scripts.cms_etl as cms_etl
#%%
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1
}


with DAG('cms_etl_pipeline', default_args=default_args, schedule_interval='@weekly', catchup=False) as dag:
    download_task = PythonOperator(
        task_id='download_data',
        python_callable=cms_etl.download_data,
        dag=dag
    )
    '''
    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=cms_etl.clean_data,
        dag=dag
    )
    '''
    load_task = PythonOperator(
        task_id='load_to_db',
        python_callable=cms_etl.load_to_db,
        dag=dag
    )

    dbt_run = BashOperator(
    task_id='dbt_run',
    bash_command='cd /opt/airflow/dbt && dbt run --profiles-dir .',
    dag=dag
    )


    download_task >> load_task >> dbt_run