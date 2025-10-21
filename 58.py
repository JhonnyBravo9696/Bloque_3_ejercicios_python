nombre_al = []
edad_al = []

nombre = ""
while nombre != '*':
  nombre = input("introduce tu nombre: * para salir del bucle: ")
  if nombre == '*':
    break
  edad = int(input("introduce tu edad: "))
  nombre_al.append(nombre)
  edad_al.append(edad)
print (f'{nombre_al} tienen respectivamente {edad_al}')
