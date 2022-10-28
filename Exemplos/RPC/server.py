#pip install kafka-rpc
from kafka_rpc import KRPCServer

class Calculadora:

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mult( self, x, y ):
        return x * y
    
    def div( self, x, y ):
        if y != 0: return x / y
        else: return None


calculador = Calculadora()

kafka_server = KRPCServer('127.0.0.1:9092', handle=calculador, topic_name='calculadora')# verify=True, encrypt='senhasecreta')

kafka_server.server_forever()