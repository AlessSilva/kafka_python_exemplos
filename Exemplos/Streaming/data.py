#pip install Faker
from faker import Faker
fake = Faker()

def gerar_RegistroUsuario():
    
    return {
        "nome" : fake.name(),
        "endereco" : fake.address(),
        "ano" : fake.year()
    }

if __name__ == "__main__":
    print(gerar_RegistroUsuario)