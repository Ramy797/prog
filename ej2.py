#Ejercicio 2: Conversor de Moneda
#Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros. El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros, utilizando un tipo de cambio fijo.
print("bienvenido al conversor eur/usd Valor del euro a la fecha 0.98, valor del dolar 1.09")
dolar = 1.09
eur = 0.98
opcion = 0
opcion = int(input("si desea convertir de euro a dolar presione 1, si desea convertir de dolar a euro presione 2" ))
if opcion == 1:
   canteu = float (input("ingrese la cantidad de euros que desea convertir a dolares") )
   converteu = canteu * dolar
   print("la conversión es:", + converteu)
if opcion == 2:
   cantusd= float (input("ingrese la cantidad de dolares que desea convertir"))
   convertusd = cantusd * eur
   print("la cantidad de dolares es:", + convertusd)