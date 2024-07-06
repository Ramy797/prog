print("bienvenido al conversor de temperatura celcius farenheit")
celcius= 1
farenheit = 33.8
opcion = int(input("ingrese 1 si desea convertir de celsius a farenheit, ingrese 2 si desea convertir de farenheit a celcius: "))
if opcion == 1:
    gradosC= int(input("ingrese la cantidad de grados celcius que desea convertir a farenheit: "))
    converC = gradosC * 1.8 + 32
    print(f"el resultado es:", converC)
if opcion == 2:
    gradosF= int(input("ingrese la cantidad de grados Farenheit que desea convertir a Celcius: "))
    ConverF= gradosF - 32 * 0.5556
    print (f"el resultado de conversión es:",round( ConverF,2))