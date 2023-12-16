#Ingrese u caracter e indicar si es vocal o no 
char=input("ingrese una vocal: ").lower() #el metodo lower() convierte la mayus en minus
if char == 'a' or char=='e' or char=='i' or char=='o' or char =='u':
  print(f"{char} es una vocal")
else:
  print(f"{char} no es una vocal")