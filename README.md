Este repositório, demonstra o uso de Herança e Polimorfismo em Python, utilizando classes que representam diferentes animais.


Estrutura de Arquivos
Animal.py     # Classe base (superclasse)
Cachorro.py   # Classe Cachorro (herda de Animal)
Cobra.py      # Classe Cobra (herda de Animal)
Galo.py       # Classe Galo (herda de Animal)
Gato.py       # Classe Gato (herda de Animal)
Vaca.py       # Classe Vaca (herda de Animal)
Main.py       # Arquivo principal para executar o programa


Conceitos Envolvidos
1. Classe Base (Superclasse)

A classe Animal define os atributos e métodos genéricos que todos os animais compartilham:

emitir_som()

locomover()



2. Herança

Cada animal (Cachorro, Cobra, Galo, Gato, Vaca) herda da classe Animal e pode adicionar comportamentos ou atributos próprios, como raca, escamas, espora, cor_pelagem, chifre.



3. Polimorfismo

O polimorfismo permite que diferentes classes redefinam o mesmo método de maneiras distintas.
Por exemplo:

O cachorro sobrescreve emitir_som() para latir.

A cobra sobrescreve emitir_som() para sibilo.

O galo sobrescreve emitir_som() para cocoricó.

O gato sobrescreve emitir_som() para miar.

A vaca sobrescreve emitir_som() para mugir.

No Main.py, todos os objetos são tratados como Animal, mas cada um executa o seu comportamento próprio:




for animal in animais:
    animal.emitir_som()
    animal.locomover()




Como Executar

No terminal, digite: python Main.py


Saída esperada (exemplo):
Totó está latindo: Au au!
Totó está correndo na rua!
Celeste diz sibilando: Sssss!
Celeste está rastejando.
Galinzé diz Cocoricó!
Galinzé está correndo na grama!
Morfeu diz Miauu.
Morfeu O gato está andando no telhado
Alegria diz Muuuuuu.
Alegria O vaca está andando no pasto!




Conclusão

Este projeto mostra de forma simples como aplicar:

Herança para reaproveitar código.

Sobrescrita de métodos para personalizar comportamentos.

Polimorfismo para tratar objetos diferentes de forma uniforme.