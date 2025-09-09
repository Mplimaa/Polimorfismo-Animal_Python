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
print(cachorro1.especie())#chama metodo asbtrato da classe mae sem precisar criar objeto cachorro1

cobra1.emitir_som()
cobra1.locomover()
print(cobra1.especie())#chama metodo asbtrato da classe mae sem precisar criar objeto cachorro1

galo1.emitir_som()
galo1.locomover()
print(galo1.especie())#chama metodo asbtrato da classe mae sem precisar criar objeto cachorro1

gato1.emitir_som()
gato1.locomover()
print(gato1.especie())#chama metodo asbtrato da classe mae sem precisar criar objeto cachorro1

vaca1.emitir_som()
vaca1.locomover()
print(vaca1.especie())#chama metodo asbtrato da classe mae sem precisar criar objeto cachorro1

