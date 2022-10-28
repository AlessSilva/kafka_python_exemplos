#pip install kafka-python
from kafka import KafkaProducer
import json
from data import gerar_RegistroUsuario
import time

# #Senha SASL/PLAIN
# producer = KafkaProducer( bootstrap_servers=['127.0.0.1:9092'], value_serializer = lambda value: json.dumps(value).encode(), 
# security_protocol='SASL_PLAINTEXT',sasl_mechanism='PLAIN', sasl_plain_username='admin', sasl_plain_password='admin-secret' )

producer = KafkaProducer( bootstrap_servers=['127.0.0.1:9092'], value_serializer = lambda value: json.dumps(value).encode() )

if __name__ == "__main__":

    while True:

        registro = gerar_RegistroUsuario()
        print(registro)

        #Caso 1
        producer.send( "usuarios", registro )

        #Caso 2

#         letra = registro["nome"][0]

#         if letra > "R":

#             print("Registro enviado para partição 2 (STUVWXYZ)")
#             producer.send( "teste3", registro, partition=2 )

#         elif letra > "J":

#             print("Registro enviado para partição 1 (KLMNOPQR)")
#             producer.send( "teste3", registro, partition=1 )

#         else:

#             print("Registro enviado para partição 0 (ABCDEFGHJ)")
#             producer.send( "teste3", registro, partition=0 )

        # producer.send( "usuarios2", registro )

        # producer.send( "topico3", registro, partition=0 )
        
        
        time.sleep(3)
