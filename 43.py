cadena = input("introduce texto: ")
caracter = input("introduce un unico caracter: ")

contador = 0
for tecla in cadena:
  if tecla == caracter:
    contador +=1

print (f'el caracter {caracter} aparece {contador} veces')

