class Animal:
	def __init__(self,especie,edat):
		self.especie=especie
		self.edat=edat
	def xerrar(self):
		pass
	def mourem(self):
		pass
	def quisoc(self):
		print("Sóc un animal del tipus {}".format(self.especie))
class Cavall(Animal):
	def xerrar(self):
		print("El so que em caracterítza és: Íiiiii")
	def mourem(self):
		print("Em moc trotant!")
class Dofí(Animal):
	def xerrar(self):
		print("El so que em caracterítza és: Txas!")
	def mourem(self):
		print("Em moc nadant!")
class Abella(Animal):
	def xerrar(self):
		print("El so que em caracterítza és: Bzzzz!")
	def mourem(self):
		print("Em moc volant")
	def picar(self):
		print("Si em molestes et picaré!")
class Humà(Animal):
	def __init__(self, especie, edat, nom):
		super().__init__(especie, edat)
		self.nom=nom
	def xerrar(self):
		print("El so que em caracterítza és: la paraula Hola!")
	def mourem(self):
		print("Em moc Caminant")
	def quisoc(self):
		print("Sóc un humà i em dic {}".format(self.nom))
class Fiet(Humà):
	def __init__(self, especie, edat, nom, pares):
		super().__init__(especie, edat,nom)
		self.pares=pares
	def nompares(self):
		print("El me pare es diu {} i la meva mare {}".format(self.pares[0], self.pares[1]))
class Centaure(Cavall, Humà):
	def quisoc(self):
		print("Sóc un centaure i sorgeix de {}".format(Centaure.__mro__))
class Xou:
	def quisoc(self):
		print("Duck type, això és el que sóc")
	def mourem(self):
		print("Duck type, així em moc")
	def xerrar(self):
		print("Duck type, així xerr")

f = [Humà("Humà",32,"Joan"), Cavall('mamífer', 10), Dofí('mamífer', 23), Abella('insecte', 1), Fiet("Humà",6,"Pau",("Joan","Luz")), Xou(), Centaure("Centaure",40,"Quiron")]
for e in f:
	e.quisoc()
	e.mourem()
	e.xerrar()
if type(e)==Fiet:
	e.nompares()
if type(e)==Abella:
	e.picar()