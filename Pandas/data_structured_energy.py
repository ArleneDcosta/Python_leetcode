import pandas as pd

sensordf = pd.read_csv('Complex_Sensor_Dataset.csv')
print(sensordf.dtypes)

sensordf['Timestamp'] = pd.to_datetime(sensordf['Timestamp'])
print(sensordf.dtypes)
print(sensordf)