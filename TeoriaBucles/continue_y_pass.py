# print("USO DEL CONTINUE:")
# number="123-456-789"
# #se buscara mostara el numero sin los guiones
# for i in number:
#   #no mostrar cuando aparece los guiones
#   if i=="-":
#     continue
#   print(i,end="")

print("USO DEL PASS:")

for i in range(12,19):
  #el pass no permite mostrar el numero 15
  if i<15:
    pass
  else:
   print ("Estos son mayores a 15:")
  print(i)

#tbm se usan cuando aun no se definen el codigo de las funciones
def funcionPrueba():
  pass 