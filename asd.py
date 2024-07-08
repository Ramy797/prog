nroF = int(input("ingrese el número al cual desea calcular su factorial: "))
contF = nroF
cont= 0
factorial = 0
suma = 0

while contF > 1:
    if cont == 0:
     cont +=1
     contF = contF - 1

     factorial = (nroF -1) * nroF 

        
    if cont > 0:
        factorial = (contF - 1) * factorial
        contF -=1

    


resultado = factorial
    
print(resultado)