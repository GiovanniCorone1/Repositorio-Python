#Muestre por consola las vocales abiertas de una palabra
#Utiliza el metodo lower() por si alguien introduce las vocales en mayuscula
palabra = input("Ingrese una palabra: ").lower()

# Variable para indicar si la palabra contiene vocales
vocales = False #dado que si no existe vocales tendria que ser false para que entre al if
for i in palabra:
    if i in "aeo":
        vocales = True
        print(i)

# Si la palabra no contiene vocales, mostrara las consonantes
if not vocales:
    for i in palabra:
        if i not in "aeo":
            print(i)

  
