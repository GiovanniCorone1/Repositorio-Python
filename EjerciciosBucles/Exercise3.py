#Mostrar la tabla de multiplicar según se introduzca la cantidad
print("\t Tabla de multiplicar")
number=int(input("Ingrese el numero del cual quiere ver la tabla: "))
if number>0:
  for i in range(0,13):
    resultado=i*number
    print(f"{number} x {i} ={resultado}" )

else:
  print("Los resultados seran 0")
