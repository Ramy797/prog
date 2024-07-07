'''''
Ejercicio 7: Juego de Adivinar el Número 
Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo.
El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo.
El juego debe continuar hasta que el jugador adivine correctamente el número.
'''
import random
print("bienvenido al juego para adivinar un número aleatorio")
nroSecreto = random.randint(1,101)
cont=0

while True:
    cantIntentos = cont
    NumUsuario= int(input("ingrese un numero entre 1 y 100: "))
    if NumUsuario == nroSecreto:
        print(f"CORRECTO HAS ADIVINADO EL NÚMERO",+ nroSecreto , "GANASTE!")
        print("te tomo :",+cantIntentos , "intentos")
        break
    if NumUsuario > nroSecreto:
        print("el Número ingresado es muy grande. intente con uno mas pequeño: ")
    if NumUsuario < nroSecreto:
        print("el Número ingresado es muy pequeño. Pruebe con uno mas grande: ")
    cont = cont + 1
