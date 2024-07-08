"""
Ejercicio 9: Calculadora de Factorial 
Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. 
El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n.
El programa debe manejar números enteros grandes y mostrar el resultado.

print("¡bienvenido a la calculadora Factorial!")
cont=1
nroF = int(input("ingrese el número al cual desea calcular su factorial"))
resultado = 1
while cont <= nroF:
    if cont == 1:
        factorial = nroF -1 * nroF
    else:
        factorial = nroF - cont * nroF
    
    
    resultado *=factorial    
    cont +=1
    
print(resultado)
"""
print("bienvenido a la calculadora de factorial")
cont = 1
resultado = 1
nroFac = int(input("ingrese el numero al cual desea calcular su factorial: "))
while cont <= nroFac:
    factorial = cont
    resultado *=factorial
    cont += 1
print(resultado)

