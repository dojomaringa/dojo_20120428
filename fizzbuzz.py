def fizzbuzz(numero):
  retorno = ""
  
  if numero % 3 == 0:
    retorno += "fizz"
  
  if numero % 5 == 0:
    retorno += "buzz"

  return retorno or str(numero)