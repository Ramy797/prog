#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
'''
import re
print("bienvenido al generador de contraseña. Para que la misma sea valida debe tener al menos 8 caracteres, al menos una mayúscula, una minúscula, un número y un caracter especial !#$%&?¡")

while True:
    contrasena= str(input("ingrese la contraseña con los requisitos necesarios"))
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&?¡]).{8,}$'
    if re.match(patron,contrasena):
        print("la contraseña ingresada es valida")
        break
    else:
        print("la contraseña ingresada no cumple con los requisitos, intente nuevamente")
'''        
import re

print("Bienvenido al generador de contraseña. Para que la misma sea válida debe tener al menos 8 caracteres, al menos una mayúscula, una minúscula, un número y un caracter especial !#$%&?¡")

while True:
    contrasena = input("Ingrese la contraseña con los requisitos necesarios: ")

    # Definir el patrón de la expresión regular
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!#$%&?¡]).{8,}$'

    # Verificar si la contraseña cumple con el patrón
    if re.search(patron, contrasena):
        print("La contraseña ingresada es válida.")
        break
    else:
        print("La contraseña ingresada no cumple con los requisitos, intente nuevamente.")



