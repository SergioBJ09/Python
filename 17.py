def invertir(a):
    b=list(a)
    c=b[::-1]
    r= "".join(c)
    return r

def palindromo(a):
  c=invertir(a)
  x=0
  for i in range(len(a)):
    if a[i]!=c[i]:
      x+=1
  if x == 0:
    return True
  else:
    return False

a=input("Introduce una palabra: ")
if palindromo(a):
  print("Es palindromo")
else:
  print("No es palindromo")