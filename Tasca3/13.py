class animal:
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad=edad
    def hablar(self):
        pass
    def mover(self):
        pass
    def quiensoy(self):
        print("Soy un {}".format(self.especie))
class caballo(animal):
    def hablar(self):
        print("HiIIIiiiIi")
    def mover(self):
        print("*galopa*")
class delfin(animal):
    def hablar(self):
        print("*chas!*")
    def mover(self):
        print("nadar")
class abeja(animal):
    def hablar(self):
        print("Bzzzz")
    def mover(self):
        print("vuela")
    def picar(self):
        print("Si molestas te pico")
class humano(animal):
    def hablar(self):
        print("Hola")
    def mover(self):
        print("caminar")
    def __init__(self,especie,edad,nombre):
        super().__init__(especie,edad)
        self.nombre=nombre
    def nombre(self):
        print("Soy humano y me llamo Pepe")