'''Hacer un programa que simule un cajero automático con un saldo inicial de $1000 
y tendrá el siguiente menú de opciones: 
1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir'''
print("\t Cajero automatico")
saldo_inicial=1000
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
opcion=int(input("Elija la opción que necesite: "))
if opcion==1:
  monto=float(input("Ingrese el monto a ingresar: "))
  print(f"${monto} ingresado")
elif opcion==2:
  retiro=float(input("Ingrese el monto a retirar: "))
  if 0<retiro<=1000:
    print("Retirando...")
    print(f"Usted retiro ${retiro}")
  elif retiro==0:
    print("Retirando...")
    print("No retiro dinero")
  elif retiro>1000:
    print("No cuenta con dinero insuficiente")
  else :
    print("Cantidad no valida")
elif opcion==3:
  print(f"Su dinero disponible es ${saldo_inicial}")
elif opcion==4:
  print("Saliendo del sistema...")
else:
  print("Error ,no es una opción")