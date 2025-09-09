from Animal import Animal
from typing import override

class Gato(Animal):
    def __init__(self, nome, idade, cor_pelagem):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.cor_pelagem = cor_pelagem # Atributo específico do Gato

    @override
    def emitir_som(self):
        # Sobrescreve o método para o gato
        print(f"{self.nome} diz Miauu.")
    
    @override
    def locomover(self):
        # Implementação genérica
        print(f"{self.nome} O gato está andando no telhado")

    @override
    def especie(cls):
        return "Felino"

