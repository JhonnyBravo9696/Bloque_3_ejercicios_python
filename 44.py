frase = input("escribe una frase: ")

contador = 1
for caracter in frase:
  if caracter == ' ':
    contador +=1

print (f' la frase tiene {contador} palabras')

