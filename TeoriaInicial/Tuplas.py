#los elementos de una tupla se puede poner con parentesis o no
mitupla=("Giovanni",17,8,True)
#mostrar algun elemento de la tupla al igual que las listas
print(mitupla[2]) #mostrara el 8

#mostrar la cantidad de elementos que hay de ese tipo(lo dentro el parentesis)
print(mitupla.count(8)) #saldra 1

#mostrar la cantidad de elementos de la tupla
print(len(mitupla)) #mostrara 4

#convertir una tupla a lista
mitupla1=("Elvis",23)
myList=list(mitupla1) #funcion "list" lo convierte
print(myList)

#convertir lista a tupla
myList1=[12.5,'e']
mitupla2=tuple(myList1) #funcion "tuple" lo convierte
print(mitupla2)

#saber si un elemento se encuentra en la tupla
print("Giovanni" in mitupla) #deber True

"""Desapaquetado de tuplas permite que cada elemento se 
pueda guardar en una variable segun el orden
de las variables"""
nombre,number1,number2,booleano=mitupla
#mostramos las variables
print("El nombre es ",nombre)
print("El primer numero es :",number1)
print("El segundo numero es :",number2)
print("El booleano es ",booleano)


