import random
print("bienvenido al juego del ahoracado")
palabrasFaciles = ["casa","hola","nube","chau","cara"]
palabrasIntermedias = ["python","cadena","regreso","murcielago","lechuga","calamar","elefante","guitarra","teclado","cocodrilo","abecedario"]
palabrasDificiles = ["hipopótamo", "espectáculo", "extraordinario", "elefanteide", "inconstitucional", "paralelepípedo", "burocráticamente", "desarrolladores", "electrodoméstico", "constitucionalidad", "esternocleidomastoideo", "contrarrevolucionario"]
dificultad=int(input("ingrese la dificultad deseada 1) Facil, 2)Intermedio, 3)Dificil"))

palabraSecreta = []
if dificultad ==1:
    palabraSecreta = random.choice(palabrasFaciles)
if dificultad ==2:
    palabraSecreta = random.choice(palabrasIntermedias)
if dificultad ==3:
    palabraSecreta = random.choice(palabrasDificiles)
cantidadLetras = len(palabraSecreta)
vidas = 6
print(f"la palabra tiene:", +cantidadLetras,"letras")
letrasPalabraSec = list(palabraSecreta)
#print(letrasPalabraSec)
letrasAdivinadas = ["_"] * len(letrasPalabraSec)
acierto=0

while vidas >0:
    if acierto == cantidadLetras:
        print("ganaste")
        break
    intento1=input("ingrese una letra: ").lower()
    if len(intento1)==1 & intento1.isalpha():    
        if intento1 in letrasPalabraSec:
                for i in range(len(letrasPalabraSec)):
                    if letrasPalabraSec[i]== intento1:
                        letrasAdivinadas[i] = intento1
                        
                print(letrasAdivinadas)        
                acierto += 1        
        else:
                print("la letra:" +intento1, "es incorrecta")
                vidas -= 1
                print("te quedan", + vidas, "vidas")
    else:
        print("ingresa un caracter correcto")            
    if vidas == 0:
        print("♫perdiste perdiste no hay nadie peor que vos♫")
