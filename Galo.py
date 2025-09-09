from Animal import Animal
from typing import override

class Galo(Animal):
    def __init__(self, nome, idade, espora):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.espora = espora # Atributo específico do Gato

    @override
    def emitir_som(self):
        # Sobrescreve o método para o gato
        print(f"{self.nome} diz Cocoricó!")
    
    @override
    def locomover(self):
        # Implementação genérica
        print(f"{self.nome} está correndo na grama!")

    @classmethod
    def especie(cls):
        return "Ave"
