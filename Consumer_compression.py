import json
import asyncio
from kafka.common import KafkaError
from aiokafka import AIOKafkaConsumer

def deserializer(serialized):
    return json.loads(serialized)

loop = asyncio.get_event_loop()
# consumer will decompress messages automatically
# in accordance to compression type specified in producer
consumer = AIOKafkaConsumer(
    'test', loop=loop,
    bootstrap_servers='localhost:9092',
    value_deserializer=deserializer,
    auto_offset_reset='earliest')
loop.run_until_complete(consumer.start())
data = loop.run_until_complete(consumer.getmany(timeout_ms=10000))
for tp, messages in data.items():
    for message in messages:
        print(type(message.value), message.value)
loop.run_until_complete(consumer.stop())
loop.close()