edad=int(input("Ingrese su edad :"))
if 0<edad<100:
  print("Edad correcta")
  if edad>18:
    print("Usted es mayor de edad")
  else:
    print("Usted es menor de edad")
else:
  print("Edad incorrecta")