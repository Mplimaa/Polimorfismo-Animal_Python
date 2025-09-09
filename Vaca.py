from Animal import Animal
from typing import override

class Vaca(Animal):
    def __init__(self, nome, idade, chifre):
        super().__init__(nome, idade) # Chama o construtor da classe pai
        self.chifre = chifre # Atributo específico do Gato

    @override
    def emitir_som(self):
        # Sobrescreve o método para o gato
        print(f"{self.nome} diz Muuuuuu.")
    
    @override
    def locomover(self):
        # Implementação genérica

        print(f"{self.nome} O vaca está andando no pasto!")

   @override
    def especie(cls):
        return "Mamífero"

