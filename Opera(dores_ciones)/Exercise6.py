'''
Construir un programa que simule el funcionamiento de una calculadora 
que puede realizar las cuatro operaciones aritméticas básicas
(suma, resta, multiplicación y división). El usuario debe especificar la operación 
con el primer carácter  del nombre de la operación.
S, s --> Suma
R, r --> Resta
P, p, M, m --> Multiplicación
D, d --> División'''
print("\t Calculadora básica")
number1=float(input("Ingrese el primer número: "))
number2=float(input("Ingrese el segundo número: "))
print("Sean las operaciones y sus símbolos:")
print("S, s --> Suma")
print("R, r --> Resta")
print("P, p, M, m --> Multiplicación")
print("D, d --> División")
char=input("Ingrese el caracter que represente la operación: ").lower()
if char== 's':
  suma=number1+number2
  print(f"La suma es {suma}")
elif char=='r':
  resta=number1-number2
  print(f"La resta es {resta}")
elif char=='p'or char=='m':
  product=number1*number2
  print(f"La multiplicación es {product}")
elif char=='d':
  division=number1/number2
  print(f"La división es {division}")
else:
  print("Caracter incorrecto")