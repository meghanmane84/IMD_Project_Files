#importing packages
from tkinter import EXCEPTION
from airflow import DAG, utils, configuration
from airflow.operators import bash_operator, branch_operator, dummy_operator, email_operator, python_operator
from datetime import date, datetime, time, timedelta
from airflow.utils.state import State
from airflow.operators.dummy_operator import DummyOperator
import pandas as pd

#for data importing


#actual DAG codes

#to check its daily working
def trigger_alert():
    raise EXCEPTION('Daily alert system test')

#to alert when the task is completed
def unfail_task(context):
    ti=context['ti']
    ti.state = State.SUCCESS    

#basic dag file
dag= DAG(
    dag_id='imd_prototype',
    description='Test alert',
    schedule_interval='@daily',
    start_date=datetime(2021, 9, 5),
    default_args={ 
        'owner': 'airflow',
        'retries':'0',
    },
    catchup=False,
)    

#basic task file
op= python_operator(
    task_id='dag1',
    python_callable=trigger_alert,
    dag=dag,
    execution_timeout=timedelta(seconds=60),
    priority_weight=100,
    on_failure_callback=unfail_task,
)