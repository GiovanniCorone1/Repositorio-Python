#Hallar la raíz cuadrad de un numero
import math
number=float(input("Ingrese un numero positivo: "))
while number<0:
  print("Error el numero no es positivo")
  number=float(input("Ingrese un numero positivo: "))
 #sqrt() para hallar la raiz cuadrada,el :.3f indica los decimales que tendra
print(f"La raiz cuadrada de {number} es {math.sqrt(number):.3f}")