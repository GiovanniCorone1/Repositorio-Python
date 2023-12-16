#FORMA-->clave:valor
miDiccionario={"Pais":"Alemania",17:18,True:False}
print(miDiccionario ) #mostramos todo el diccionario
#cantidad de elementos de un diccionario
print(len(miDiccionario))
#valores del diccionario
print(miDiccionario.values()) 
#claves del diccionario
print(miDiccionario.keys()) 

#si queremos mostrar solo el valor 
print(miDiccionario["Pais"]) #se mostrara el valor "Alemania"

#Agregar elementos al diccionario
miDiccionario["Agregado"]="Listo"
print(miDiccionario)

#sobreescribir/cambiar un valor
miDiccionario["Agregado"]="cambiado"
print(miDiccionario)

#eliminar clave:valor del diccionario
del miDiccionario[17] #se utiliza funcion "del"
print(miDiccionario)

'''Creamos un diccionario donde cada elemento de una tupla
 sea la el valor 
'''
miTupla=("nombre","entero","flotante")
miDiccionario1={miTupla[0]:"Giovanni",miTupla[1]:12,miTupla[2]:19.5}
print(miDiccionario1)

#diccionarios ,tuplas y listas dentro de un diccionario
miDiccionario2={"años":{"pares":[2022,2024]}}
miDiccionario3={"impares":(13,15,17)}
print(miDiccionario2) #muestra todo el diccionario(valor :clave)
print(miDiccionario2["años"]) #muestra el diccionario:{"pares" ...}
'''Para mostrar la lista de miDiccionario2 se debe
a las clave de ese diccionatrio ,luego a la clave 
del diccionario que esta dentro'''
print(miDiccionario2["años"]["pares"]) #muestra la lista
print(miDiccionario3["impares"]) #muestra la tupla



