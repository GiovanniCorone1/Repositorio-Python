print("\t Asignaturas aperturadas")
print("Arquitectura de Computadoras-Computacion Visual-Algoritmica II")
curso=input("Escribe la asignatura: ")
asignatura=curso.lower() #el metodo lower() convierte todo en minuscula
if asignatura in ("arquitectura de computadoras","computacion visual","algoritmica II"):
  print(f"Matriculado en {asignatura}")
else:
  print("Curso no aperturado") 
