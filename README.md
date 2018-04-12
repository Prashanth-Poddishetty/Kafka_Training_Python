# Kafka_Training_Python


Here are well designed Python scripts which can help you get started with Kafka-Python. 

Following are the list of topics that are covered with these examples:
 - Kafka Producer reading records from File.
 - Kafka Producer fetching records from MySql Database.
 - Kafka Consumer injecting records to MySql Database.
 - Encoding and Decoding Kafka messages in producer and consumer
 - Serialization and Deserialization of Kafka messages in Producer and Consumer.
 - Compression and Decompression of Kafka records in producer and consumer. 

Following are the list of scripts present in the repo:

  - FileAsSource.py : This is a producer file, which reads records from a file and send them as messages to consumer.
  - MysqlAsSource.py: This is a Producer file, which reads records from a MySql Database and send them as messages to consumer. The records are encoded when sent to consumer.
  - MysqlAsSink.py: This is a Consumer file, which injects the received records into MySql Database. The records are decoded at the consumer end.
  - ConsumerCompression.py: The records which are received are decompressed based on the compression type used in the Producer. 
  - ProducerCompression.py: The records are compressed using compressin type gZip. The compressed message are sent to consumer. 
