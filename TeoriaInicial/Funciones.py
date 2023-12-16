#FUNCIONES SIN PARAMETRO
#definimos a la funcion
print("Funciones sin parametro:")
def nombre_funcion():
  print("hello")
#llamamos a la funcion
nombre_funcion()

#FUNCIONES CON PARAMETRO
#definimos a la funcion
print("funciones con parametro:")
def suma(number1,number2):
  print(number1+number2)
#llamamos a la funcion
suma(5,2)
print("más código...")
#se reutiliza la funcion pero con otros parametros 
suma(8,9.5)

#Funciones que devuelven un valor
def resta(a,b):
  resultado=a-b
  return resultado
print(resta(55,22))