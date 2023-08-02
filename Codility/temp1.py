import os
os.environ['os.env']='secret'

print (os.environ.get('os.env'))


from kafka import KafkaProducer
import logging
from json import dumps, loads
import csv



producer = KafkaProducer(bootstrap_servers='127.0.0.1:9092', value_serializer=lambda K:dumps(K).encode('utf-8'))

with open('home/ak/proj/new/Latestdata.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for messages in reader:
       producer.send('Finances', messages)
       producer.flush()
