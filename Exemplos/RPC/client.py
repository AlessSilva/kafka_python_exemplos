#pip install kafka-rpc
from kafka_rpc import KRPCClient

kafka_client = KRPCClient('127.0.0.1:9092', topic_name='calculadora')#, verify=True, encrypt='senhasecreta')

print(kafka_client.add(7, 2))
print(kafka_client.sub(7,2))
print(kafka_client.mult(7,2))
print(kafka_client.div(7,2))

kafka_client.close()