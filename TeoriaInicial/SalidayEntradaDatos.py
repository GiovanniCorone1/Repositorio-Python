nombre="Giovanni"
edad=18
nota=19.5
#formas de salida de datos
print("Mi nombre es ",nombre,"tengo ", edad," me saque ",nota) #primera forma
#segunda forma
print("Mi nombre es {} y tengo {} y saque {} en ADA".format(nombre,edad,nota))
#tercera forma
print(f"Mi nombre es {nombre} y tengo {edad}, saque {nota} en ADA")


#Entrada de datos
#valores cadena (str)
nombre1=input("Ingrese su nombre: ")
#valores enteros (int)
edad1=int(input("Ingrese su edad: "))
#valores decimales(float)
estatura=float(input("Ingrese su estatura: "))
#mostramos todos los datos guardados
print(f"Mi nombre es {nombre1} y tendo {edad1},mido {estatura} ")
