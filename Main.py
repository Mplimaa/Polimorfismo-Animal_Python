from Cachorro import Cachorro
from Cobra import Cobra
from Galo import Galo
from Gato import Gato
from Vaca import Vaca

cachorro1  = Cachorro("Totó", 7, raca = "Pastor Alemão")
cobra1 = Cobra("Celeste", 5 , escamas="Laranja")
galo1 = Galo("Galinzé", 6 , espora="De aço")
gato1 = Gato("Morfeu", 5 , cor_pelagem="Preto e Branco" )
vaca1 = Vaca("Alegria", 7, chifre="Não tem")

# Lista de animais
animais = [cachorro1, cobra1, galo1, gato1, vaca1]

# Iterando sobre a lista e chamando o mesmo método para todos
for animal in animais:
    animal.emitir_som()
    animal.locomover()
    animal.especie()


cachorro1.emitir_som()
cachorro1.locomover()
cachorro1.especie()

cobra1.emitir_som()
cobra1.locomover()
cobra1.especie()

galo1.emitir_som()
galo1.locomover()
galo1.especie()

gato1.emitir_som()
gato1.locomover()
gato1.especie()

vaca1.emitir_som()
vaca1.locomover()
vaca1.especie()

