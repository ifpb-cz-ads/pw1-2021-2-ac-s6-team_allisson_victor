n = int(input("Tabuada de: "))
x = int(input("Tabuada ate o numero: "))
controle = 0
while controle <= x:
    resultado = n*controle
    print(n,"x", controle,"=",resultado)
    controle += 1