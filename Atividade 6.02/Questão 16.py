n = int(input("Informe o número:"))
aux = n
cont= 0
while aux > 0 : 
    
   if n%aux == 0 :
        cont+=1
   aux -= 1
if cont == 2 :
    print("O numero %d é primo"%n)
else :
    print("O numero %d não é primo"%n)     