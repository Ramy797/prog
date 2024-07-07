'''
Ejercicio 8: Generador de Contraseñas Aleatorias 
Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de 
letras (mayúsculas y minúsculas), números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.
'''
import random
print("bienvenido al generador de contraseñas aleatorias")

largoContrasena = int(input("ingrese el largo de su contraseña. el mismo no puede ser menor a 12"))
contrasena = []
while len(contrasena) < largoContrasena:
    contrasena = "" 
    contrasena.append(random.choice("qwertyuiopasdfghjklñzxcvbnm"))
    contrasena.append(random.choice("QWERTYUIOPASDFGHJKLÑZXCVBNM"))
    contrasena.append(random.choice("0123456789"))
    contrasena.append(random.choice("!#$%&/()=?¡"))
    if contrasena == largoContrasena:
        break
print(contrasena)