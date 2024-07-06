#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
import re
print("bienvenido al generador de contraseña. Para que la misma sea valida debe tener al menos 8 caracteres, al menos una mayúscula, una minúscula, un número y un caracter especial !#$%&?¡")
contrasena= str(input("ingrese la contraseña con los requisitos necesarios"))
validaciones= "A-Z", "a-z", "0-9", "!#$%&/()=?"
correcta = re.search(validaciones, contrasena)
print(correcta.group())
