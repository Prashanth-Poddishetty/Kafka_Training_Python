from kafka import KafkaProducer
#from kafka.errors import KafkaError
#from kafka.producer.kafka import log
import os
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

location = os.path.join(os.path.expanduser('~'),'Documents','Sample-text')

file = open(location,'r')
data = file.readline()
print(data)
#producer.send('test',b'test msg')
while data:

    producer.send('test', json.dumps(data).encode('utf-8'))
    data = file.readline()


# configure multiple retries
producer = KafkaProducer(retries=5)