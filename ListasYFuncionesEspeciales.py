myList=["Giovanni",False,23,19.5,"a"]
myList2=["pi",2]
#agregar un lemento al final de la lista
print(myList.append("agregado")) #mostrar la lista final

#agregar un elemento a la lista pero especificando la posición
myList.insert(2,"insertado")
print(myList) #mostrar la lista final

#agregar una lista al final de la otra
myList.extend(["Elvis",12,True])
print(myList)

#mostrar el indice de una elemento de la lista
print(myList.index("Giovanni"))

#para saber si un elemento se encuentra en la lista
print(19.5 in myList)  #debe imprimir true,ya que ,si esta en la lista
print(77 in myList)  #debe imprimir false,ya que ,no esta en la lista

#estas ultimas funciones no se pueden poner dentro del print ya que no sale lo pedido
#eliminar algun elemento de la lista
myList.remove(12) #indicammos el elemento
print(myList)
#Eliminar el ultimo elemento de la lista
myList.pop()
print(myList)

#unimos dos listas
myList3=myList+myList2
print(myList3)

#duplicamos(2),triplicamos(3),etc una lista
myList4=["Gane",12]*2 
print(myList4)
