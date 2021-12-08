#15) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
# Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.
i=1
while i != 0:
    print("")
    print("----Menu----")
    print("Digite 1 para ver a tabuada de adição")
    print("Digite 2 para ver a tabuada de subtração")
    print("Digite 3 para ver a tabuada de multiplicação")
    print("Digite 4 para ver a tabuada de divisão")
    print("Digite 0 para sair")
    print("")
    opcao = int(input("Escolha uma das opções: "))
    
    if opcao == 1: 
        x = 1
        n = int(input("Digite o numero da tabuada: "))
        while x <= 10:
            resultado = n + x
            print(n ,"+",x, "=", resultado)
            x=x+1
    if opcao == 2: 
        x = 1
        n = int(input("Digite o numero da tabuada: "))
        while x <= 10:
            resultado = x - n
            print(x ,"-",n, "=", resultado)
            x=x+1
    if opcao == 3: 
        x = 1
        n = int(input("Digite o numero da tabuada: "))
        while x <= 10:
            resultado = n * x
            print(n ,"x",x, "=", resultado)
            x=x+1
    if opcao == 4: 
        x = 1
        n = int(input("Digite o numero da tabuada: "))
        while x <= 10:
            resultado = (x*n) / n
            print(x*n ,"/",n, "=", resultado)
            x=x+1
    i=opcao