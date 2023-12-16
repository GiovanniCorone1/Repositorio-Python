print("Caso :Diccionarios")
diccionario={"pais":"Alemania","numero":20}
for i in diccionario:
  #mostramos todo el diccionario(clave:valor)(2 veces/2elementos)
  #i muestra las claves del diccionario
  #{diccionario[i]} muestra los valores del diccionario
  print(f"{i}-->{diccionario[i]} del {diccionario}")

print("\t ----- ")
   
#Otra forma de mostara la clave:valor del diccionario
#es el metodo items() y dos valores que recorren el diccionario
for clave , valor in diccionario.items():
  print(clave,"-->",valor)
