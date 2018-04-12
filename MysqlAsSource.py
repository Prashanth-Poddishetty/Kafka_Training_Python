import json
from kafka import KafkaProducer
import pymysql.cursors

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='root',
                                     db='datasource',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = "Select * from emp"
cursor.execute(sql)
rows = cursor.fetchall()
data = ""

for row in rows:
    data = str(row['empno']) + '|' + row['ename'] + '|' + row['job']
    producer.send('test', json.dumps(data).encode('utf-8'))
    data = ""

cursor.close()
connection.close()

# configure multiple retries
producer = KafkaProducer(retries=5)