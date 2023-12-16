"""Con funciones:Si un alumno saca mayor o igual a 10.5 debe estar aprobado
caso contrario desaprobado"""
print("\tEstado del alumno")
nota_Alumno = input("Ingrese su nota: ")

def evaluacion(nota):
    estadoNota = "Alumno aprobado"
    if nota <10.5:
        estadoNota = "Alumno desaprobado"
    return estadoNota

print(evaluacion(int(nota_Alumno)))
