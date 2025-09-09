from Animal import Animal
from typing import override

class Cobra(Animal):
    def __init__(self, nome, idade, escamas):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.escamas = escamas # Atributo específico da classe filha

    @override
    def emitir_som(self):
        # Sobrescreve o método para classe filha
        print(f"{self.nome} diz sibilando: Sssss!")
    
    @override
    def locomover(self):
        # Sobrescreve o método para classe filha
        print(f"{self.nome} está rastejando.")

    @classmethod
    def especie(cls):
        return "Reptil"
