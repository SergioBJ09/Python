def longitud(valor):
    # Simple validación. No aceptamos otra cosa que no sea
    # una lista (list) o una cadena (str)
    if type(valor) is not list and type(valor) is not str:
        return -1
    # Contador que vamos incrementando en cada iteración
    contador = 0
    # Mientras haya datos que iterar, aumentar el contador
    # Nota: si es str, iteramos letra por letra.
    # si es list, iteramos elemento por elemento
    for elemento in valor:
        contador += 1
    return contador


# Probar
cadena = input("Introduce la cadena: ")
print("Longitud de cadena:", longitud(cadena))