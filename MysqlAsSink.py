from kafka import KafkaConsumer
import json
import msgpack
import pymysql.cursors
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('test',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'])

connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='root',
                                     db='datasource',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()


for message in consumer:
    #print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, message.value))
    x = str(message.value.decode('utf-8')).split('|')
    print(message.value.decode('utf-8'))
    print(x)
    sql = "insert into emp1 values(%s, %s, %s)"
    cursor.execute(sql, ( int(x[0].replace('"', "")), x[1], x[2].replace('"', "")))
    connection.commit()

connection.commit()
connection.close()


# StopIteration if no message after 1sec
KafkaConsumer(consumer_timeout_ms=100)


