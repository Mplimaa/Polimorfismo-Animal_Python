from Animal import Animal
from typing import override

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.raca = raca # Atributo específico da classe filha

    @override
    def emitir_som(self):
        # Sobrescreve o método para classe filha
        print(f"{self.nome} está latindo: Au au!")

    
    @override
    def locomover(self):
        # Sobrescreve o método para classe filha
        print(f"{self.nome} está correndo na rua!")