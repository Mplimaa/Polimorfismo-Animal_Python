from Cachorro import Cachorro
from Cobra import Cobra
from Galo import Galo
from Gato import Gato
from Vaca import Vaca

Cachorro = Cachorro("Totó", 7, raca = "Pastor Alemão")
Cobra = Cobra("Celeste", 5 , escamas="Laranja")
Galo = Galo("Galinzé", 6 , espora="De aço")
Gato = Gato("Morfeu", 5 , cor_pelagem="Preto e Branco" )
Vaca = Vaca("Alegria", 7, chifre="Não tem")

# Lista de animais
animais = [Cachorro, Cobra, Galo, Gato, Vaca]

# Iterando sobre a lista e chamando o mesmo método para todos
for animais in animais:
    animais.emitir_som()
    animais.locomover()


Cachorro.emitir_som()
Cachorro.locomover()

Cobra.emitir_som()
Cobra.locomover()

Galo.emitir_som()
Galo.locomover()

Gato.emitir_som()
Gato.locomover()

Vaca.emitir_som()
Vaca.locomover()

