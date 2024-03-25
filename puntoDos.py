
print('************************************************')
recibirNumero = int(input("Digite la cantidad de frutas para el salpicón: "))
print('************************************************')

frutas = []

for i in range(recibirNumero):
  
  idFruta = int(input(f"Digite el ID de la fruta {i+1}: "))
  nombreFruta = input(f"Digite el nombre de la fruta {i+1}: ")
  precioUnitario = int(input(f"Digite el precio unitario de la fruta {i+1}: "))
  cantidadFruta = int(input(f"Digite la cantidad de la fruta {i+1}: "))
    
  frutas.append({
    "id": idFruta,
    "nombre": nombreFruta,
    "precioUnitario": precioUnitario,
    "cantidad": cantidadFruta
  })

costoTotal = 0
for fruta in frutas:
  costoTotal += fruta["precioUnitario"] * fruta["cantidad"]

def ordenar(frutas):

  n = len(frutas)

  for i in range(n-1):
   
    for j in range(0, n-i-1):
      if frutas[j]["precioUnitario"] * frutas[j]["cantidad"] < frutas[j + 1]["precioUnitario"] * frutas[j + 1]["cantidad"]:
        frutas[j], frutas[j + 1] = frutas[j + 1], frutas[j]


ordenar(frutas)

frutaMasBarata = frutas[-1]


opcion=None

while opcion != 4:
  print("---------------------------------------------------")
  print("Opciones:")
  print("1. Mostrar costo total del salpicón")
  print("2. Mostrar frutas ordenadas de mayor a menor costo")
  print("3. Mostrar cual fue la fruta mas barata")
  print("4. Salir")
  print("---------------------------------------------------")

  opcion = int(input("Digite la opción deseada: "))

  if opcion == 1:
    print(f"Costo total del salpicón: ${costoTotal}")
  elif opcion == 2:
    print("Frutas ordenadas de mayor a menor costo:")
    for fruta in frutas:
      print(f"- {fruta['nombre']}: ${fruta['precioUnitario']} x {fruta['cantidad']} = ${fruta['precioUnitario'] * fruta['cantidad']}")
  elif opcion == 3:
    print(f"La fruta más barata es: {frutaMasBarata['nombre']}")
  else:
    print("Opción inválida.")
