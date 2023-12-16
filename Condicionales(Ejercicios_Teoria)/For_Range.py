#Metodo range()=indica el intervalo de repeticiones,donde el "i" toma valores dependiendo de ese rango
cantidad=int(input("Ingrese la cantidad de repeticiones: "))
for i in range(cantidad): #i=0,1,2...cantidad-1
  print("Repeticion",i)
print("--Range(inico,fin)--")
for i in range(2,4):  #i E (2,4>
  print(i) #2,3
print("--Range(inicio,fin,salto)--")
for i in range(4,10,3): #range(inicio,final,saltos)
  print(i) #i=4,7


