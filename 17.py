igual, aux = 0, 0
texto = input("Ingrese la palabra: ")
for ind in reversed(range(0, len(texto))):
  if texto[ind].lower() == texto[aux].lower():
    igual += 1
  aux += 1
if len(texto) == igual:
  print("Es palindromo")
else:
  print("No es palindromo")