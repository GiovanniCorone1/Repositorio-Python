""" Hacer un menú que considere las siguientes opciones:
	Caso 1: Cubo de un numero
	Caso 2: Numero par o impar
	Case 3: salir.
"""
import math
print("\t Sea el menu de opciones")
print("""1.Cubo de un numero
2.Numero es par o no
3.salir""")
opcion=int(input("Elige una opcion: "))
match opcion:
  case 1:
    number=int(input("Ingrese el numero :"))
    potencia=pow(number,3)
    print(f"El cubo de {number} es {potencia}")
  case 2:
    number=int(input("Ingrese un numero: "))
    if number%2==0:
      print(f"El numero {number} es par")
    else:
      print(f"El numero {number} es impar")
  case 3:
    print("Saliendo del programa ...")
  case _:
    print("No es una opcion")
print("Programa terminado ")

