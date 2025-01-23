class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        return "Som genérico de animal"


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome)
        self.raca = raca

    def fazer_som(self):
        return "Au Au!"


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome)
        self.cor = cor

    def fazer_som(self):
        return "Miau!"


cachorro = Cachorro("Rex", "Labrador")
gato = Gato("Miau", "Branco")

print(f"O cachorro {cachorro.nome} da raça {cachorro.raca} faz o som: {cachorro.fazer_som()}")
print(f"O gato {gato.nome} de cor {gato.cor} faz o som: {gato.fazer_som()}")
