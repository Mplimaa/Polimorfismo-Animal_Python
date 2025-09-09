from abc import ABC, abstractmethod  # ← Import necessário
#abc = Abstract Base Classes (Módulo interno do Python).
#ABC → transforma a classe em abstrata (não pode ser instanciada).
# abstractmethod → marca métodos que devem ser implementados pelas classes filhas.


# Classe mãe (superclasse)
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        # Implementação genérica
        print("O animal está fazendo um som.")
    
    def locomover(self):
        # Implementação genérica
        print("O animal está se locomovendo.")

    @classmethod
    @abstractmethod
    def especie(cls):
        pass





