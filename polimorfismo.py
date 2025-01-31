class Animal:
    def fazer_som(self):
        raise NotImplementedError("Subclasse deve implementar este metodo!")

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au Au Au Au Au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau Miau Miau Miau Miau"

class Calopsita(Animal):
    def fazer_som(self):
        return "AHhhh AHhhh AHhhh"

# Função para emitir os sons dos animais
def emitir_sons(animais):
    for animal in animais:
        print(animal.fazer_som())

cachorro = Cachorro()
gato = Gato()
calopsita = Calopsita()

animais = [cachorro, gato, calopsita]
emitir_sons(animais)