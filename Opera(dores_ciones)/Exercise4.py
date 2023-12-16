#en este programa los pasos son de elif a elif (arriba a abajo)
nota=float(input("Ingrese su nota"))
if 0<nota<5:
  print("Insuficiente")
elif 0<nota<6:
  print("Suficiente") 
elif 0<nota<7:
  print("Bien")
elif 0<nota<9:
  print("Notable")
else: #este else se concatena con el anterior if(del elif)
  print("Sobresaliente") 