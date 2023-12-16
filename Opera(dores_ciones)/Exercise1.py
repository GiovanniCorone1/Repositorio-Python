"""si un alumno saca mayor o igual a 10.5 debe estar aprobado
caso contrario desaprobado"""
print("\t Estado de alumno")
nota_alumno=float(input("Ingrese su nota : "))
if nota_alumno>=10.5:
  print("Alumno aprobado")
else :
  print("Alumno desaprobado")