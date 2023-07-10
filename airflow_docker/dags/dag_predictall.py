from airflow import DAG
from airflow.utils.dates import days_ago
import requests
from airflow.operators.python import PythonOperator
import datetime


my_dag = DAG(
    dag_id='predictall_assets',
    description='API Request from Myapp',
    tags=['myapp', 'abdullahcay'],
    start_date=datetime.datetime(2023,7,9),
    default_args={
        'owner': 'airflow'},
    schedule_interval='0 0 * * *'
)


# definition of the API address
api_address = '192.168.1.17'
# API port
api_port = 9090


# requests
# definition of the function to execute
def get_api_predictall():
    #end_point = 'predictall'
    print(datetime.datetime.now())
    url01  = 'http://192.168.1.17:9090/api/predictall'
    #url01 = f'http://{api_address}:{api_port}/api/{end_point}'
    response = requests.get(url= url01)
    data = response.json()
    return data


task1 = PythonOperator(
    task_id='get_api_predictall',
    python_callable=get_api_predictall,
    dag=my_dag
)