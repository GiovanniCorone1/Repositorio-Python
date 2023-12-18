#num1,num2 son parametros / number1 ,number2 son argumentos
#son buenas practicas de programacion que sean de diferentes nombres
#Buena practica:definir y luego llamar a la funcion
num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))
def multiplicar(number1,number2):
  #es buena practica que la multiplacion se guarde en una variable
  multiplicacion=number1*number2
  return multiplicacion,"El producto es " #Se puede retornar varios valores
producto,cadena=multiplicar(num1,num2)
print(f"{cadena}{producto}")
