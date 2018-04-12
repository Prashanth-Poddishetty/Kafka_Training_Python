import json
import asyncio
from aiokafka import AIOKafkaProducer

def serializer(value):
    return json.dumps(value).encode()

@asyncio.coroutine
def produce(loop):
    producer = AIOKafkaProducer(
        loop=loop, bootstrap_servers='localhost:9092',
        value_serializer=serializer,
        compression_type="gzip")

    yield from producer.start()
    data = {"a": 123.4, "b": "some string"}
    yield from producer.send('test', data)
    data = [1,2,3,4]
    yield from producer.send('test', data)
    yield from producer.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(produce(loop))
loop.close()