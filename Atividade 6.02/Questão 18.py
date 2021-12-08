n1 = int(input("Digite o primeiro número :"))
n2 = int(input("Digite o segundo número :"))
aux = 0
resultado = n1
resto = 0
while resultado>0:
    if(resultado>n2):
        aux+=1
    resultado -=n2
    if(resultado<n2):
        resto = resultado + n2
print("O resto é ", resto) 
