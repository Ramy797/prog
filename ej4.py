#Ejercicio 4: Contador de Palabras
#Desarrolla un programa en Python que solicite al usuario que ingrese una frase y luego cuente y muestre el número de palabras en esa frase.
cont=0
print("bienvenido al contador de palabras:")
frase = input("ingrese la frase a la que desea contar sus palabras")
palabras = frase.split()
print(palabras)
for palabra in palabras:
    cont = cont +1
print(cont)