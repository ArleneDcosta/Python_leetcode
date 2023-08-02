import pydoop.hdfs as hdfs
from pyspark.sql import SparkSession
from kafka import KafkaProducer, KafkaConsumer
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Apache Hadoop - Reading a file from HDFS
def read_file_from_hdfs():
    with hdfs.open("/path/to/file.txt") as file:
        data = file.read()
        print(data)

# Apache Spark - Word count example
def word_count_with_spark():
    spark = SparkSession.builder.appName("WordCount").getOrCreate()
    lines = spark.read.text("file:///path/to/file.txt")
    word_counts = lines.rdd.flatMap(lambda line: line.value.split()).countByValue()
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Apache Kafka - Producing and consuming messages
def produce_and_consume_messages():
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('my_topic', b'Hello, Kafka!')

    consumer = KafkaConsumer('my_topic', bootstrap_servers='localhost:9092')
    for message in consumer:
        print(message.value.decode('utf-8'))

# Apache Airflow - Defining a DAG and tasks
def my_function():
    print("Hello, Airflow!")

dag = DAG(
    'data_engineering_pipeline',
    description='Example data engineering pipeline',
    schedule_interval='0 0 * * *',  # Runs daily at midnight
    start_date=datetime(2023, 5, 17),
    catchup=False
)

read_file_task = PythonOperator(
    task_id='read_file_from_hdfs',
    python_callable=read_file_from_hdfs,
    dag=dag
)

word_count_task = PythonOperator(
    task_id='word_count_with_spark',
    python_callable=word_count_with_spark,
    dag=dag
)

produce_consume_task = PythonOperator(
    task_id='produce_and_consume_messages',
    python_callable=produce_and_consume_messages,
    dag=dag
)

my_function_task = PythonOperator(
    task_id='my_function_task',
    python_callable=my_function,
    dag=dag
)

read_file_task >> word_count_task >> produce_consume_task >> my_function_task
