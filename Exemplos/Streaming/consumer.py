#pip install kafka-python
from kafka import KafkaConsumer
import json
import time
from kafka.structs import TopicPartition

if __name__ == "__main__":

    

    # Caso 1 : Ler todas as mensagens do início (earliest) 
    #Caso 2: Ler apenas depois da última (latest)
    # consumer = KafkaConsumer("usuarios", bootstrap_servers='127.0.0.1:9092', auto_offset_reset="earliest"
    #                         , group_id="grupo_a", value_deserializer = lambda value: json.loads(value))

    consumer = KafkaConsumer(bootstrap_servers='127.0.0.1:9092', auto_offset_reset="earliest"
                           , group_id="grupo_g", value_deserializer = lambda value: json.loads(value))
    topic = "teste3"
    consumer.assign([TopicPartition(topic, 0)])

    #Senha SASL/PLAIN
    # consumer = KafkaConsumer( "usuarios", bootstrap_servers='127.0.0.1:9092', auto_offset_reset="latest"
    #                         , group_id="grupo_A", value_deserializer=lambda value: json.loads(value),
    #                         security_protocol='SASL_PLAINTEXT',sasl_mechanism='PLAIN', sasl_plain_username='admin', sasl_plain_password='admin-secret')

    for msm in consumer:

        data : dict = msm.value
        
        print("Registro: ", data)
        
        time.sleep(3)