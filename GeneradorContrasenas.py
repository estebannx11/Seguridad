import string
import random

def generar_contrasena(longitud):
    #Todos los caracteres posible con la libreria string para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    #Observar los caracteres posibles de la contraseña
    #print(caracteres)
    #Concatenar caracteres de forma aleatoria  con la longitud desiganada por el user
    contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

while True:
    try:
        longitud = int(input("Por favor ingrese el tamaño de la contraseña: "))
        if longitud > 0:
            break
        else:
            print("La longitud de la contraseña debe de ser un número positivo.")
    except:
        print("Por favor ingrese un número valido")

contrasena_generada = generar_contrasena(longitud)
print("La contraseña generada es: " + contrasena_generada)